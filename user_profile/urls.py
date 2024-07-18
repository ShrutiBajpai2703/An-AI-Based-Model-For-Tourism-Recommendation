from django.conf.urls import url, include
from . import views
from .views import home2
from django.urls import path

urlpatterns = [
    url(r'^accounts/profile/$', views.UserProfileView.as_view(), name="profile"),
    url(r'^accounts/status/$', views.UserStatusView.as_view(), name="status"),
    path('home2/', home2, name='home2'),

    path('state_detail/', views.state_detail, name='state_detail'),
    path('recommend_place/', views.recommend_place, name='recommend_place'),
    path('recommend_place_mood/', views.recommend_place_mood, name='recommend_place_mood'),
    path('recommend_mood_result/', views.recommend_mood_result, name='recommend_mood_result'),
    path('add_place/', views.add_place, name='add_place'),
    path('save_review/', views.save_review, name='save_review'),
    
    


]
