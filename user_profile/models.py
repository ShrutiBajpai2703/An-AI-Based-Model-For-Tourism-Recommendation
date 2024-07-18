from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.base import ContentFile
from io import BytesIO

from django_thumbs.fields import ImageThumbsField  # Import ImageThumbsField from django_thumbs
from django.utils import timezone
import logging
import os
import itertools
import math
import operator
from collections.abc import Callable, Iterable
from functools import partial
from typing import Iterator, Optional, Sequence
from placeholder import partials

__version__ = '1.5'

import pkg_resources
import random
from PIL import Image, ImageFont, ImageDraw


class PlaceholderPic(object):

    DEFAULT_FONT_FILE = pkg_resources.resource_filename(
        __name__, 'SourceSansPro-Regular.ttf')

    DEFAULTS = {
        'size': 300,
        'foreground': '#ffffff',
        'background': None,
        'font_file': DEFAULT_FONT_FILE,
        'font_size': None,
    }

    # https://www.google.com/design/spec/style/color.html#color-color-palette
    BACKGROUNDS = [
        '#F44336',  # Red
        '#E91E63',  # Pink
        '#9C27B0',  # Purple
        '#673AB7',  # Deep purple
        '#3F51B5',  # Indigo
        '#2196F3',  # Blue
        '#03A9F4',  # Light Blue
        '#00BCD4',  # Cyan
        '#009688',  # Teal
        '#4CAF50',  # Green
        '#8BC34A',  # Light Green
        '#CDDC39',  # Lime
        '#FFEB3B',  # Yellow
        '#FFC107',  # Amber
        '#FF9800',  # Orange
        '#FF5722',  # Deep Orange
        '#795548',  # Brown
        '#9E9E9E',  # Grey
        '#607D8B',  # Blue Grey
    ]

    @classmethod
    def random_color(self):
        return "#%06x" % random.randint(0, 0xFFFFFF)

    def __init__(self, text, **kwargs):
        self.text = text
        options = PlaceholderPic.DEFAULTS.copy()
        options.update(**kwargs)
        if options['background'] is None:
            options['background'] = random.choice(PlaceholderPic.BACKGROUNDS)
        if options['background'].lower() == 'random':
            options['background'] = PlaceholderPic.random_color().upper()
        if options['font_size'] is None:
            options['font_size'] = int(options['size']/2)
        for key, value in options.items():
            setattr(self, key, value)
        self._image = None

    @property
    def image(self):
        if self._image is None:
            self._image = Image.new(
                mode='RGB',
                size=(self.size, self.size),
                color=self.background)
            draw = ImageDraw.Draw(self._image)
            font = ImageFont.load_default()
            text_width =  draw.textlength(self.text, font=font)
            text_height = draw.textlength(self.text, font=font)
            draw.text(
                (
                    (self.size-text_width)/2,
                    (self.size-text_height*1.275)/2,
                ),
                self.text,
                self.foreground,
                font=font)
        return self._image

def update_wrapper(wrapper: Callable, func: Callable):
    wrapper.__doc__ = func.__doc__
    wrapper.__name__ = func.__name__
    wrapper.__annotations__['return'] = 'F'
    return wrapper


def pipe(funcs: Sequence[Callable], *args, **kwargs):
    value = funcs[0](*args, **kwargs)
    for func in funcs[1:]:
        value = func(value)
    return value


def methods(func: Callable):
    def left(self, other):
        if isinstance(other, F):
            return type(self)(self, func)
        return type(self)(self, partials.partial(func, other).left)

    def right(self, other):
        return type(self)(self, partials.partial(func, other).right)

    return update_wrapper(left, func), update_wrapper(right, func)


def unary(func: Callable):
    return update_wrapper(lambda self: type(self)(self, func), func)


class F(partial):
    """Singleton for creating composite functions.

    Args:
        *funcs (Callable): ordered callables
    """

    def __new__(cls, *funcs):
        funcs = (func if isinstance(func, cls) else [func] for func in funcs)
        funcs = tuple(itertools.chain(*funcs))
        return partial.__new__(cls, *(funcs if len(funcs) == 1 else (pipe, funcs)))

    def __iter__(self) -> Iterator[Callable]:
        """Return composed functions in order."""
        args = super().__getattribute__('args')
        return iter(args[0] if args else [super().__getattribute__('func')])

    def __getattribute__(self, attr: str) -> 'F':
        """Return `attrgetter`."""
        if attr.startswith('__') and attr.endswith('__'):
            return super().__getattribute__(attr)
        return type(self)(self, operator.attrgetter(attr))

    def __getitem__(self, item) -> 'F':
        """Return `itemgetter`."""
        return type(self)(self, operator.itemgetter(item))

    def __round__(self, ndigits: Optional[int] = None) -> 'F':
        """Return `round(...)`."""
        return type(self)(self, round if ndigits is None else partial(round, ndigits=ndigits))

    __neg__ = unary(operator.neg)
    __pos__ = unary(operator.pos)
    __invert__ = unary(operator.invert)

    __abs__ = unary(abs)
    __reversed__ = unary(reversed)

    __trunc__ = unary(math.trunc)
    __floor__ = unary(math.floor)
    __ceil__ = unary(math.ceil)

    __add__, __radd__ = methods(operator.add)
    __sub__, __rsub__ = methods(operator.sub)
    __mul__, __rmul__ = methods(operator.mul)
    __floordiv__, __rfloordiv__ = methods(operator.floordiv)
    __truediv__, __rtruediv__ = methods(operator.truediv)

    __mod__, __rmod__ = methods(operator.mod)
    __divmod__, __rdivmod__ = methods(divmod)
    __pow__, __rpow__ = methods(operator.pow)
    __matmul__, __rmatmul__ = methods(operator.matmul)

    __lshift__, __rlshift__ = methods(operator.lshift)
    __rshift__, __rrshift__ = methods(operator.rshift)

    __and__, __rand__ = methods(operator.and_)
    __xor__, __rxor__ = methods(operator.xor)
    __or__, __ror__ = methods(operator.or_)

    __eq__ = methods(operator.eq)[0]
    __ne__ = methods(operator.ne)[0]
    __lt__, __gt__ = methods(operator.lt)
    __le__, __ge__ = methods(operator.le)


class M:
    """Singleton for creating method callers and multi-valued getters."""

    def __getattr__(cls, name: str) -> F:
        """Return a `methodcaller` constructor."""
        return F(partial(operator.methodcaller, name), F)

    def __call__(self, *names: str) -> F:
        """Return a tupled `attrgetter`."""
        return F(operator.attrgetter(*names))

    def __getitem__(self, keys: Iterable) -> F:
        """Return a tupled `itemgetter`."""
        return F(operator.itemgetter(*keys))


_ = F()
m = M()

logger = logging.getLogger(__name__)

# Create your models here.
def upload_avatar_to(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'userprofile/%s%s' % (
        timezone.now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )


class UserProfile(models.Model):
    SIZES = (
        {'code': '60x60', 'wxh': '60x60', 'resize': 'crop'},  #
        {'code': '100x100', 'wxh': '100x100', 'resize': 'crop'},
        {'code': '200x200', 'wxh': '200x200', 'resize': 'crop'},  # 'resize' defaults to 'scale'
        {'code': '400x400', 'wxh': '400x400', 'resize': 'crop'},  # 'resize' defaults to 'scale'
    )

    THUMBNAIL_ALIASES = {
        '': {
            'avatar': {'size': (50, 50), 'crop': True},
        },
    }

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    image = ImageThumbsField(default=None, verbose_name="profile image",
                             sizes=SIZES,
                             upload_to=upload_avatar_to, null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True, default=None, verbose_name="Write about your self")
    location = models.CharField(max_length=30, blank=True, null=True, default=None)
    birth_date = models.DateField(null=True, blank=True)

    def generate_img(self):
        f = BytesIO()
        logger.debug("generating image")
        if self.user.first_name:
            img_name = self.user.first_name[:2].capitalize()
        else:
            img_name = self.user.email[:2].capitalize()
        placeholder = PlaceholderPic(img_name)
        placeholder.image.save(f, format='png')
        s = f.getvalue()

        self.image.save("%s.png" % self.user.id,
                        ContentFile(s))


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)
        if not profile.image:
            profile.generate_img()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.user_profile.save()


from django.db import models

class UserReview(models.Model):
    state_name = models.CharField(max_length=30, blank=True, null=True, default=None)
    review_text = models.TextField()
    rating = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
