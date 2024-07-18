from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.shortcuts import redirect, reverse
from user_profile.forms import UserProfileModelForm, UserDetailModelForm


# Create your views here.


class UserProfileView(TemplateView, LoginRequiredMixin):
    template_name = "user_profile/profile.html"

    def post(self, request, *args, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user_profile_form'] = user_profile_form = UserProfileModelForm(request.POST, request.FILES,
                                                                                instance=request.user.user_profile)
        context['user_detail_form'] = user_detail_form = UserDetailModelForm(request.POST,
                                                                             instance=request.user)
        if user_profile_form.is_valid() and user_detail_form.is_valid():
            user_profile_form.save()
            user_detail_form.save()
            return redirect(reverse('profile'))
        else:
            print(user_profile_form.errors, "++++++")

        return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user_profile_form'] = UserProfileModelForm(instance=request.user.user_profile)
        context['user_detail_form'] = UserDetailModelForm(instance=request.user)
        return render(request, self.template_name, context=context)


class UserStatusView(TemplateView, LoginRequiredMixin):
    template_name = "user_profile/status.html"

def home2(request):
    return render(request, 'home2/home2.html')

from django.shortcuts import render

from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse







datavalue = {
    'Andhra Pradesh': [
        {'place': 'Charminar','long':17.361570,'lat':78.474663 ,'temp':29,'type': 'Historical','details':'Charminar - It is a historical monument and mosque located in the heart of Hyderabad. Built in 1591 by the fifth ruler of the Qutb Shahi dynasty, Mohammed Quli Qutb Shah, it is a popular tourist attraction and one of the most recognized landmarks of Hyderabad.' ,'url':'https://www.wonderwardrobes.com/wp-content/uploads/2015/06/Charminar-898x1024.jpg'},
        {'place': 'Tirumala Venkateswara Temple','long':13.683080,'lat':79.350365 , 'temp':26, 'type': 'Religious','details':'Tirumala Venkateswara Temple - It is a world-famous Hindu temple located on the hills of Tirumala in the state of Andhra Pradesh, about 20 km from the city of Tirupati in Chittoor district. It is one of the richest and most visited temples in India.' ,'url':'https://th.bing.com/th/id/OIP.1NEN7YnH9hztWWLzujbPGgHaEA?pid=ImgDet&rs=1'},
        {'place': 'Golconda Fort','long':17.383310,'lat':78.401047 , 'temp':27, 'type': 'Historical','details':'Golconda Fort - It is a historical fort located in Hyderabad. The fort was originally built in the 13th century by the Kakatiya dynasty and was later expanded by the Qutb Shahi dynasty. The fort is famous for its acoustics and its unique design, which allows sound to be heard from a distance of almost a kilometer.' ,'url':'https://th.bing.com/th/id/R.67efcb7734d2bb4f7f2401ac87868276?rik=uU%2fOZQyXe5wdtg&riu=http%3a%2f%2fwww.thesoultrails.com%2fwp-content%2fuploads%2f2018%2f11%2fGolconda-Fort-Hyderabad-Monuments-Heritage-3.jpg&ehk=Bh6YeDuKuhsp7poFXTT%2biB%2f8e3cmcl08%2bVey9wj7C%2f4%3d&risl=&pid=ImgRaw&r=0'},
        {'place': 'Araku Valley','long':18.303730,'lat':82.909300 , 'temp':27, 'type': 'Hill Station','details':'Araku Valley - It is a hill station located in the Visakhapatnam district of Andhra Pradesh. It is famous for its scenic beauty and is surrounded by lush green forests, waterfalls, and coffee plantations. The valley is also home to various tribes and is known for its rich cultural heritage.' ,'url':'https://th.bing.com/th/id/OIP.wK8N06IlwV2n2Gy-6b2brwAAAA?pid=ImgDet&rs=1'},
        {'place': 'Ramoji Film City','long':17.252913,'lat':78.680443 , 'temp':29, 'type': 'Entertainment','details':'Ramoji Film City - It is a large film studio complex located in Hyderabad. It is one of the largest film studios in the world and has been certified by the Guinness World Records. The complex features various film sets, amusement parks, and live shows. It is a popular tourist attraction and a must-visit for movie enthusiasts.' ,'url':'https://th.bing.com/th/id/OIP.Krmwe2oszvwtAmrYNyPkPgHaFQ?pid=ImgDet&rs=1'},
    ],
    'Arunachal Pradesh': [
        {'place': 'Tawang Monastery','long':27.585531,'lat': 91.857216 , 'temp':21, 'type': 'Religious','details':'Tawang Monastery: It is a famous Buddhist monastery situated in Tawang district of Arunachal Pradesh. It is also known as the Galden Namgyal Lhatse Monastery and is one of the largest monasteries in India. The monastery was built in the 17th century by Mera Lama Lodre Gyatso. The monastery has a beautiful architecture and is an important center of Buddhist learning.' ,'url':'https://mynortheast.files.wordpress.com/2009/05/85.jpg'},
        {'place': 'Bomdila Monastery','long':27.270559,'lat': 92.418510 , 'temp':18, 'type': 'Religious','details':'Bomdila Monastery: It is a popular Buddhist monastery located in the West Kameng district of Arunachal Pradesh. The monastery was built in the year 1965 and is situated at an altitude of about 8000 feet above sea level. The monastery has a beautiful structure and is an important center of Buddhist learning.' ,'url':'https://indiano.travel/wp-content/uploads/2022/03/Beautiful-front-view-of-Bomdila-Monastery.jpg'},
        {'place': 'Sela Pass','long':27.504810,'lat':92.104700 , 'temp':12, 'type': 'Scenic','details':'Sela Pass: It is a high-altitude mountain pass located on the border of the Tawang and West Kameng districts of Arunachal Pradesh. It is situated at an altitude of about 13,700 feet above sea level and offers stunning views of the surrounding mountains and valleys. The pass is covered with snow for most of the year and is a popular destination for adventure seekers.' ,'url':'https://static-blog.treebo.com/wp-content/uploads/2019/08/Sela-Pass-Tawang.jpg'},
        {'place': 'Namdapha National Park','long':27.443541,'lat':96.535576 ,  'temp':24,'type': 'Wildlife','details':'Namdapha National Park: It is a beautiful national park situated in the Changlang district of Arunachal Pradesh. The park is known for its rich biodiversity and is home to a wide variety of flora and fauna, including the Bengal tiger, clouded leopard, Indian elephant, and hornbill. The park also has a large number of bird species, making it a paradise for bird watchers.' ,'url':'https://visatoexplore.in/wp-content/uploads/2020/06/DSC_7621.jpg'},
        {'place': 'Pangsau Pass','long':27.247600,'lat': 96.156000 , 'temp':20 , 'type': 'Scenic','details':'Pangsau Pass: It is a mountain pass located on the border of Arunachal Pradesh and Myanmar. The pass is situated at an altitude of about 3,727 feet above sea level and offers stunning views of the surrounding mountains and valleys. The pass is an important trade route between India and Myanmar and is also known for its natural beauty.' ,'url':'https://i.pinimg.com/originals/d0/05/bd/d005bdb02eb24e5d88c75fcd06e271bf.jpg'},
        
    ],
    'Assam': [
        {'place': 'Kaziranga National Park','long':26.577543,'lat':93.171127 , 'temp':24 , 'type': 'Wildlife','details':'Kaziranga National Park: This park is famous for its one-horned rhinoceros, tigers, elephants, and other wildlife. It is also home to numerous bird species. Visitors can go on jeep and elephant safaris to explore the park.' ,'url':'https://newslivetv.com/wp-content/uploads/2020/10/EkWMMyXU8AUl3yc.jpg'},
        {'place': 'Manas National Park','long':26.780481,'lat':90.960274 , 'temp':24 , 'type': 'Wildlife','details':'Manas National Park: This park is a UNESCO World Heritage Site and is known for its Bengal tigers, elephants, and clouded leopards. It also has a rich biodiversity, with over 450 species of birds and many species of plants.' ,'url':'https://th.bing.com/th/id/R.61651500a3c55b57d00a69c5b0f74ac6?rik=05XXK1k51h35kw&riu=http%3a%2f%2fwww.thesoultrails.com%2fwp-content%2fuploads%2f2020%2f06%2fManas-National-Park-Assam-Bodoland-Soul-Trails-17.jpg&ehk=nKqcpXD2oKTlIN%2bpt7jXFGHUAtT%2fBo4%2b6VDR2IuVLkU%3d&risl=&pid=ImgRaw&r=0'},
        {'place': 'Kamakhya Temple','long':26.166420,'lat':91.705147 , 'temp':24 , 'type': 'Religious','details':'Kamakhya Temple: This temple is dedicated to the goddess Kamakhya and is a popular pilgrimage site. It is located on a hill in Guwahati and has a unique architecture. Visitors can also witness the annual Ambubachi Mela, a fertility festival held here.' ,'url':'https://th.bing.com/th/id/R.08e5fca57591feb4e293bbe1d9a7e4ff?rik=fBm4UmH6CaSPTw&riu=http%3a%2f%2fcdn.findmessages.com%2fimages%2f2016%2f07%2f158-kamakhya-temple-at-guwahati.jpg&ehk=n747002hRKIZ35bdef7Lgxbk0YG4ODUz9Uiwy7QYXRw%3d&risl=&pid=ImgRaw&r=0'},
        {'place': 'Sualkuchi','long':26.169320,'lat': 91.572640 , 'temp':24 , 'type': 'Cultural','details':'Sualkuchi: This town is known for its silk weaving industry and is a great place to buy silk sarees and other garments. Visitors can also watch the weavers at work and learn about the process.' ,'url':'https://th.bing.com/th/id/R.2614f511bad1a0aca0d2d21ed154dc42?rik=E1KaXXdqVQlzsA&riu=http%3a%2f%2flyfdaily.com%2fwp-content%2fuploads%2f2017%2f09%2fDSC_0139-1024x509.jpg&ehk=%2fBBczQo%2b28b7X4uWZTZugFISU95%2b2y560DSn9AuIuKs%3d&risl=&pid=ImgRaw&r=0'},
        {'place': 'Majuli Island','long':26.950000,'lat': 94.166700 , 'temp':24 , 'type': 'Scenic','details':'Majuli Island: This river island is the largest in the world and is located in the Brahmaputra River. It is known for its scenic beauty, wildlife, and cultural heritage. Visitors can explore the island on foot or by bicycle and learn about the local culture and traditions.' ,'url':'https://thirdeyetraveller.com/wp-content/uploads/2018/02/PC123167-2-1.jpg'},
        
    ],
    'Bihar': [
        {'place': 'Mahabodhi Temple','long':24.695940,'lat':84.991226 , 'temp':24 , 'type': 'Religious','details':'Mahabodhi Temple: It is a UNESCO World Heritage site located in Bodh Gaya, Bihar. The temple is considered one of the holiest sites for Buddhists as it is believed to be the place where Gautama Buddha attained enlightenment. The temple complex consists of the main temple, a sacred Bodhi tree, a meditation park, and several smaller shrines and monasteries. The architecture of the temple is a blend of Indian and East Asian styles.' ,'url':'https://th.bing.com/th/id/OIP.SIU9T_SW_UJpxg5_XBD_DgHaEy?pid=ImgDet&rs=1'},
        {'place': 'Patna Museum','long':25.608070,'lat':85.120987 , 'temp':24 , 'type': 'Museum','details':'Patna Museum: Located in the capital city of Patna, the Patna Museum is a popular attraction for history and art enthusiasts. The museum houses a vast collection of artifacts, including sculptures, paintings, coins, and textiles, that reflect the rich history and culture of Bihar. Some of the highlights of the museums collection are the relics of the Mauryan Empire, terracotta figurines from the ancient city of Pataliputra, and a 200-million-year-old fossil of a tree trunk.' ,'url':'https://theshillongtimes.com/wp-content/uploads/2017/04/patna-museum.jpg'},
        {'place': 'Nalanda University','long':25.135460,'lat': 85.446053 , 'temp':24 , 'type': 'Historical','details':'Nalanda University: Nalanda University was a renowned center of learning in ancient India that flourished between the 5th and 12th centuries CE. The ruins of the university are located in the town of Nalanda, about 95 km from Patna. The university was a melting pot of diverse cultures and attracted scholars and students from all over the world. The site has several temples, stupas, and monasteries that are worth visiting.' ,'url':'https://th.bing.com/th/id/R.f06420bff42511a2dc8469217286ef71?rik=bu1dURI1MCS0BA&riu=http%3a%2f%2fwww.thehistoryhub.com%2fwp-content%2fuploads%2f2014%2f04%2fNalanda-University-Pictures.jpg&ehk=1nkkjOLtBSipj7LhixurzHMuR3fvZN%2bLFPtvbwEIOec%3d&risl=&pid=ImgRaw&r=0'},
        {'place': 'Bodh Gaya','long':24.708500,'lat': 84.965900 , 'temp':24 , 'type': 'Religious','details':'Bodh Gaya: Bodh Gaya is a holy city located in the Gaya district of Bihar. It is believed to be the place where Gautama Buddha attained enlightenment under the Bodhi tree. The city is home to several important Buddhist sites, including the Mahabodhi Temple, the Bodhi tree, and several monasteries and shrines. The city also attracts tourists interested in yoga and meditation.' ,'url':'https://mediaim.expedia.com/destination/1/e8a57b5952cbb50b3f1ef30fe2613355.jpg'},
        {'place': 'Vikramshila Ruins','long':25.323997,'lat':87.284653 , 'temp':24 , 'type': 'Historical','details':'Vikramshila Ruins: The Vikramshila Ruins are the remains of an ancient Buddhist monastery that was founded during the Pala Empire (8th-12th century CE). The monastery was one of the most important centers of Buddhist learning in India and attracted scholars and students from all over the world. The ruins are located in the town of Antichak, about 40 km from Bhagalpur. The site has several temples, stupas, and meditation halls that are worth visiting.' ,'url':'https://www.bodhibihar.com/wp-content/uploads/2020/06/vikramshila-ruins.jpg'},
        
    ],
    'Chhattisgarh': [
        {'place': 'Chitrakoot Falls','long':19.206495, 'lat':81.699982 , 'temp':24 , 'type': 'Scenic','details':'Chitrakoot Falls: Known as the "Niagara Falls of India," Chitrakoot Falls is a stunning natural wonder that attracts visitors from all over the country. Located on the Indravati River, the falls are surrounded by lush greenery and are particularly beautiful during the monsoon season. Visitors can take a dip in the cool, refreshing water or enjoy a picnic on the banks of the river.' ,'url':'https://th.bing.com/th/id/R.7a2bdec24b2dff20a7a779761609ba22?rik=7HfQPdC%2f6TAZrw&riu=http%3a%2f%2fphotos.wikimapia.org%2fp%2f00%2f02%2f79%2f90%2f35_full.jpg&ehk=CHZnTGhKk04S6A1OQvVXYy%2f61UFD7URQ7VrrHPMLhHY%3d&risl=&pid=ImgRaw&r=0'},
        {'place': 'Tirathgarh Waterfall','long':18.913860, 'lat':81.865273 , 'temp':24 , 'type': 'Scenic','details':'Tirathgarh Waterfall: Another popular waterfall in Chhattisgarh, Tirathgarh is a multi-tiered waterfall that is particularly impressive during the monsoon season. The falls are surrounded by dense forests and are a popular spot for hiking and birdwatching. Bastar Palace: Located in Jagdalpur, Bastar Palace is a historical palace that was once ' ,'url':'https://www.holidify.com/images/cmsuploads/compressed/34626179432_f046b1b358_b_20190322100759.jpg'},
        {'place': 'Bastar Palace','long':19.092699, 'lat':82.022339 , 'temp':24 , 'type': 'Historical','details':'Bastar Palace: Located in Jagdalpur, Bastar Palace is a historical palace that was once the residence of the Bastar royal family. The palace is known for its stunning architecture and intricate wood carvings, and visitors can explore the many rooms and halls that make up the palace.' ,'url':'https://qph.fs.quoracdn.net/main-qimg-29b420a38a5e826fa3c0aa9c2d3cc2ce-c'},
        {'place': 'Kanger Valley National Park','long':18.779772, 'lat':82.005608 , 'temp':24 , 'type': 'Wildlife','details':'Kanger Valley National Park: Located in the Bastar district of Chhattisgarh, Kanger Valley National Park is a wildlife sanctuary that is home to a wide variety of flora and fauna. Visitors can go on safaris to spot animals like tigers, leopards, and sloth bears, or explore the parks many hiking trails.' ,'url':'https://1.bp.blogspot.com/-9wNwp9cjwqY/XmIrxWHkIAI/AAAAAAAAC5o/ksrGFvX4WrcFQzL-pFX9pquEdO5Xzxn2ACLcBGAsYHQ/s1600/kangervalleynationalpark0202020202002020.jpg'},
        {'place': 'Barnawapara Wildlife Sanctuary','long':21.450239, 'lat':82.522667 , 'temp':24 , 'type': 'Wildlife','details':'Barnawapara Wildlife Sanctuary: Another popular wildlife sanctuary in Chhattisgarh, Barnawapara is home to a wide variety of animals and birds. Visitors can go on safaris to spot animals like wild boars, deer, and leopards, or explore the parks many hiking trails. The sanctuary is also home to a large number of reptiles, including snakes and crocodiles.' ,'url':'https://d368ufu7xgcs86.cloudfront.net/25353-1585750367.jpg'},
        
    ],
    'Goa': [
        {'place': 'Baga Beach','long':15.558890, 'lat':73.753330 , 'temp':24 , 'type': 'Beach','details':'Baga Beach: Located in North Goa, Baga Beach is one of the most popular beaches in Goa. It offers a range of water sports and beachside activities like parasailing, banana boat rides, and jet skiing. There are also several shacks and restaurants along the beach, offering delicious seafood and drinks. The beach is usually crowded, especially during the peak tourist season.' ,'url':'https://static.toiimg.com/thumb/msid-59486326,width=1200,height=900/59486326.jpg'},
        {'place': 'Calangute Beach','long':15.555117,'lat': 73.756601 , 'temp':24 , 'type': 'Beach','details':'Calangute Beach: Known as the "Queen of Beaches," Calangute Beach is another popular beach in North Goa. It offers a range of water sports and activities like surfing, parasailing, and jet skiing. The beach is lined with shacks and restaurants, offering a range of food and drinks. The beach can get quite crowded during peak tourist season.' ,'url':'https://i2.wp.com/www.goacoworking.com/wp-content/uploads/2021/05/ng-Calangute-dji-4-scaled.jpg?w=2400&ssl=1'},
        {'place': 'Basilica of Bom Jesus','long':15.500900, 'lat':73.911629 , 'temp':24 , 'type': 'Religious','details':'Basilica of Bom Jesus: Located in Old Goa, the Basilica of Bom Jesus is a UNESCO World Heritage Site and one of the most famous churches in Goa. The church is known for its Baroque architecture and houses the mortal remains of St. Francis Xavier. The church attracts a large number of visitors every year and is a popular pilgrimage site for Christians.' ,'url':'https://harstuff-travel.org/wp-content/uploads/2019/05/panaji-basilica-of-bom-jesus-147713353653-orijgp.jpg'},
        {'place': 'Dudhsagar Falls','long':15.312770,'lat': 74.314163 , 'temp':24 , 'type': 'Scenic','details':'Dudhsagar Falls: Located on the Mandovi River, Dudhsagar Falls is one of the most beautiful waterfalls in India. The falls are surrounded by lush green forests and offer a breathtaking view of the cascading water. The best time to visit the falls is during the monsoon season when the falls are in full flow.' ,'url':'https://indiator.com/tourist-places/wp-content/uploads/2016/11/Awsome-View-Of-Falls-Dudhsagar-Falls.jpeg'},
        {'place': 'Fort Aguada','long':15.492510,'lat':73.773804 , 'temp':24 , 'type': 'Historical','details':'Fort Aguada: Located in North Goa, Fort Aguada is a 17th-century Portuguese fort that was built to defend against Dutch and Maratha invaders. The fort offers a panoramic view of the Arabian Sea and is surrounded by lush greenery. The fort is also home to a lighthouse, which offers a stunning view of the coastline.' ,'url':'https://www.adotrip.com/public/images/areas/5c3db276d588a-Aguada%20fort%20Package%20Tour.jpg'},
       
    ],
    'Gujarat': [
        {'place': 'Statue of Unity','long':21.837780, 'lat':73.718887 , 'temp':24 , 'type': 'Monument','details':'Statue of Unity: The Statue of Unity is the worlds tallest statue, standing at 182 meters tall. It is dedicated to Sardar Vallabhbhai Patel, who played a significant role in Indias struggle for independence. The statue is located in the Narmada district of Gujarat, and visitors can take a high-speed elevator to an observation deck at a height of 153 meters to enjoy panoramic views of the surrounding landscape. There is also a museum on the ground floor dedicated to the life and work of Sardar Vallabhbhai Patel.' ,'url':'https://blog.akbartravels.com/wp-content/uploads/2018/11/rsz_amitdavereuters.jpg'},
        {'place': 'Sabarmati Ashram','long':23.060730, 'lat':72.580818 , 'temp':24 , 'type': 'Historical','details':'Sabarmati Ashram: Sabarmati Ashram is a historical site located in the city of Ahmedabad. It was home to Mahatma Gandhi, the father of the Indian nation, from 1917 to 1930. The ashram served as the headquarters for the Indian independence movement, and Gandhi launched many of his campaigns from this site. Today, the ashram has been converted into a museum that houses a collection of Gandhis personal belongings, including his spinning wheel and his letters.' ,'url':'https://im.rediff.com/news/2016/jun/15trip-sabarmati4.jpg'},
        {'place': 'Rani ki vav','long':23.858820, 'lat':72.101936 , 'temp':24 , 'type': 'Historical','details':'Rani ki vav: Rani ki vav is an intricately designed stepwell located in the town of Patan in Gujarat. It was built in the 11th century by Queen Udayamati in memory of her husband, King Bhimdev I. The stepwell is one of the most beautiful and well-preserved examples of its kind in India and is decorated with intricate carvings depicting Hindu mythology and various gods and goddesses.' ,'url':'https://cdn.nexusnewsfeed.com/images/2020/6/Rani-ki-vav-1595024022656.jpg?w=1200&h=900'},
        {'place': 'Somnath Temple','long':21.819571, 'lat':70.021240 , 'temp':24 , 'type': 'Religious','details':'Somnath Temple: Somnath Temple is an important pilgrimage site for Hindus located on the western coast of Gujarat. It is believed to be one of the 12 jyotirlingas (lingams of light) of Lord Shiva, and it has been destroyed and rebuilt several times throughout history. The current structure dates back to 1950 and is a beautiful example of contemporary temple architecture. Visitors can attend the aarti (prayer ceremony) held at the temple in the evening and take a stroll along the nearby beach.' ,'url':'https://www.thehistoryhub.com/wp-content/uploads/2017/02/Somnath-Temple-Images.jpg'},
        {'place': 'Gir Forest National Park','long':21.124840, 'lat':70.824409 , 'temp':24 , 'type': 'Wildlife','details':'Gir Forest National Park: Gir Forest National Park is the last remaining home of the Asiatic lion and is located in the state of Gujarat. The park covers an area of 1,412 square kilometers and is home to a variety of other wildlife, including leopards, hyenas, and sambar deer. Visitors can take a safari ride through the park to catch a glimpse of these majestic creatures in their natural habitat. The best time to visit the park is between December and March.' ,'url':'https://artoftravel.tips/wp-content/uploads/2018/09/Gir-National-Park.jpg'},
        
    ],
    'Haryana': [
        {'place': 'Sultanpur National Park','long':28.467915, 'lat':76.891632 , 'temp':24 , 'type': 'Wildlife','details':'Sultanpur National Park: This wildlife sanctuary is located in Gurgaon and is home to many migratory birds. Its a great place for birdwatching and nature photography. You can also take a walk along the trails and spot some deer, peacocks, and other animals. There are also watchtowers for bird watching.' ,'url':'https://www.hindustantimes.com/rf/image_size_960x540/HT/p2/2018/09/11/Pictures/sultanpur-concluded-exhibition-showcasing-migratory-exhibition-protection_f24d035a-b54f-11e8-bbaf-ff4d73ce44e3.jpg'},
        {'place': 'Sheetla Mata Mandir','long':28.478300,'lat':77.030502 , 'temp':24 , 'type': 'Religious','details':'Sheetla Mata Mandir: This temple is dedicated to Sheetla Mata, who is considered to be the goddess of smallpox. The temple is located in Gurugram and is a popular place of worship. The temple is believed to have healing powers and attracts many devotees.' ,'url':'https://media.tripinvites.com/places/gurugram/sheetla-mata-mandir/sheetla-mata-mandir-gurugram-featured.jpeg'},
        {'place': 'Surajkund Mela','long':28.484974, 'lat':77.284950 , 'temp':24, 'type': 'Cultural','details':'Surajkund Mela: This is a popular cultural festival that takes place in Faridabad every year in February. The festival showcases the art, craft, and culture of various states of India. You can enjoy dance performances, musical shows, and sample various cuisines from across the country.' ,'url':'https://d27k8xmh3cuzik.cloudfront.net/wp-content/uploads/2017/11/Surajkund-Mela-2018-Dates.jpg'},
        {'place': 'Leisure Valley Park','long':28.469030, 'lat':77.066338 , 'temp':24, 'type': 'Recreational','details':'Surajkund Mela: This is a popular cultural festival that takes place in Faridabad every year in February. The festival showcases the art, craft, and culture of various states of India. You can enjoy dance performances, musical shows, and sample various cuisines from across the country.' ,'url':'https://www.touristplaces.net.in/images/pp/5/p100448.jpg'},
        {'place': 'Badkhal Lake','long':28.415690, 'lat':77.277920 , 'temp':24, 'type': 'Scenic','details':'Badkhal Lake: This lake is located in Faridabad and is a popular picnic spot. You can enjoy boating, fishing, and other water activities here. There are also several restaurants and cafes near the lake where you can enjoy a meal with a view. However, the lake has been facing environmental issues due to pollution, so its best to check the current status before visiting.' ,'url':'https://www.eastcoastdaily.in/wp-content/uploads/2018/05/Badhkal-lake-780x405.png'},
        ],

    'Himachal Pradesh': [
        {'place': 'Rohtang Pass','long':32.379841, 'lat':77.251495 , 'temp':24, 'type': 'Scenic','details':'Rohtang Pass: Rohtang Pass is a high mountain pass located at an altitude of 3978 meters above sea level. It is one of the most popular tourist destinations in Himachal Pradesh, offering stunning panoramic views of snow-covered mountains and glaciers. Visitors can enjoy various adventure activities here, such as skiing, snowboarding, and sledging. The pass is open from May to November, and during winter it remains closed due to heavy snowfall.' ,'url':'https://th.bing.com/th/id/R.c9ad1e044d9f38a481f1219c47f17e6b?rik=Mt06gHWQNqrzrg&riu=http%3a%2f%2fi.huffpost.com%2fgen%2f3253502%2fimages%2fo-ROHTANG-PASS-facebook.jpg&ehk=ZygO%2b5S8VPA9bcc5%2biEzw2%2bvhpQiSz1TxH3vNEjfLsg%3d&risl=&pid=ImgRaw&r=0'},
        {'place': 'The Ridge','long':31.104855, 'lat':77.174049 , 'temp':24, 'type': 'Scenic','details':'The Ridge: The Ridge is a large open space located in the heart of Shimla, the capital city of Himachal Pradesh. It offers spectacular views of the surrounding hills and valleys and is a popular spot for taking leisurely walks. The Ridge is also the venue for various cultural events and festivals throughout the year, including the Summer Festival and the Winter Carnival.' ,'url':'https://th.bing.com/th/id/R.6412df044f87872ea5bb97d0e29fc1ed?rik=iktMdXGE8rDkSA&riu=http%3a%2f%2fwww.holidify.com%2fimages%2fcompressed%2fattractions%2fattr_2357.jpg&ehk=FPArKuMOGkcLhMRH7tMCdguE7loTLUrWmUa6QDMhhm4%3d&risl=&pid=ImgRaw&r=0'},
        {'place': 'Hadimba Devi Temple','long':32.248440, 'lat':77.180809 , 'temp':24, 'type': 'Religious','details':'Hadimba Devi Temple: Hadimba Devi Temple is a popular religious site located in Manali, Himachal Pradesh. The temple is dedicated to Hidimba Devi, the wife of Bhima from the epic Mahabharata. It is known for its unique architecture, with a pagoda-style roof and intricately carved wooden doors. Visitors can also enjoy the scenic beauty of the surrounding cedar forest.' ,'url':'https://i.pinimg.com/originals/f1/81/8b/f1818b71749ffd2cc18d01a55e376430.jpg'},
        {'place': 'Kufri Fun World','long':31.094173,'lat': 77.278099 , 'temp':24, 'type': 'Recreational','details':'Kufri Fun World: Kufri Fun World is an amusement park located in Kufri, a small town near Shimla. It offers various rides and activities for visitors of all ages, such as go-karting, bungee jumping, and zip-lining. The park is surrounded by scenic views of the snow-capped Himalayan mountains.' ,'url':'https://assets.traveltriangle.com/blog/wp-content/uploads/2017/12/Kufri-Fun-World-kb6592.jpg'},
        {'place': 'Kullu Valley','long':31.944290, 'lat':77.109470 , 'temp':24, 'type': 'Scenic','details':'Kullu Valley: Kullu Valley is a picturesque valley located in the Himalayas, known for its stunning natural beauty and cultural heritage. It is surrounded by high mountains, lush green forests, and the Beas River. The valley is famous for adventure sports such as trekking, river rafting, and paragliding. It is also known for its vibrant festivals, such as the Kullu Dussehra and the Spring Festival.' ,'url':'https://thumbs.dreamstime.com/b/beas-river-kullu-valley-himachal-pradesh-india-near-manali-221304320.jpg'},
        ],

    'Jharkhand': [
        {'place': 'Hundru Falls','long':23.450001, 'lat':85.650002 , 'temp':24, 'type': 'Scenic','details':'Hundru Falls: Hundru Falls is a beautiful waterfall located in the Ranchi district of Jharkhand. It is a popular picnic spot and attracts tourists with its scenic beauty. The waterfall cascades from a height of around 98 feet and the water flows into the Subarnarekha River. Visitors can also enjoy swimming in the natural pool formed at the base of the falls.' ,'url':'https://www.tripiwiki.com/images/places/uploads/Hundru-Falls1932.jpg'},
        {'place': 'Betla National Park','long':23.873257,'lat': 84.188271 , 'temp':24, 'type': 'Wildlife','details':'Betla National Park: Betla National Park is located in the Latehar district of Jharkhand and is one of the most popular national parks in the state. The park is home to a wide variety of flora and fauna, including tigers, elephants, leopards, wild boars, and several species of birds. Visitors can go on jungle safaris and nature walks to explore the parks diverse wildlife and natural beauty.' ,'url':'https://edge.ixigo.com/ixi-api/img/5142fd76e4b09702078bd2b3_600x315.jpg'},
        {'place': 'Jagannath Temple','long':19.804699, 'lat':85.818153 , 'temp':24, 'type': 'Religious','details':'Jagannath Temple: Jagannath Temple is a famous Hindu temple located in Ranchi. The temple is dedicated to Lord Jagannath, an incarnation of Lord Vishnu. The temples architecture is inspired by the famous Jagannath Temple in Puri, Odisha, and is a popular pilgrimage site for devotees of Lord Jagannath.' ,'url':'https://www.tripsavvy.com/thmb/wdbjlbZRP1QmjHSGja3zH7qA1w0=/3559x2357/filters:fill(auto,1)/_DSC0713_Snapseed_Fotor-56a3c23a3df78cf7727f07e8.jpg'},
        {'place': 'Tilaiya Dam','long':24.323891, 'lat':85.521111 , 'temp':24, 'type': 'Scenic','details':'Tilaiya Dam: Tilaiya Dam is a popular tourist spot located near the town of Tilaiya in Jharkhand. The dam is built on the Barakar River and is surrounded by beautiful hills and forests. Visitors can enjoy boating in the reservoir, go on nature walks, and enjoy the scenic beauty of the area.' ,'url':'https://media-cdn.tripadvisor.com/media/photo-s/1a/17/da/cc/tilaiya-dam.jpg'},
        {'place': 'Hirni Falls','long':22.866700, 'lat':85.333300 , 'temp':24, 'type': 'Scenic','details':'Hirni Falls: Hirni Falls is another beautiful waterfall located in the Ranchi district of Jharkhand. It is a popular picnic spot and attracts tourists with its natural beauty. The waterfall cascades from a height of around 35 feet and the water flows into the Subarnarekha River. Visitors can enjoy swimming in the natural pool formed at the base of the falls.' ,'url':'https://media-cdn.tripadvisor.com/media/photo-s/18/40/af/ec/hirni-falls.jpg'},
        ],

    'Karnataka': [
        {'place': 'Mysore Palace','long':12.305300, 'lat':76.654800 , 'temp':24 ,'type': 'Historical','details':'Mysore Palace: This historical palace is located in the city of Mysore, and is one of the most popular tourist attractions in Karnataka. It was once the residence of the Wodeyar dynasty, and is now a museum that showcases the history and culture of the region. The palace is known for its impressive architecture and intricate designs, and is especially beautiful when lit up at night.' ,'url':'https://d2rdhxfof4qmbb.cloudfront.net/wp-content/uploads/20191003134442/Maharajahs-Palace-in-Mysore.jpg'},
        {'place': 'Hampi','long':15.326810, 'lat':76.466960 ,'temp':24 , 'type': 'Historical','details':'Hampi: This UNESCO World Heritage Site is located in the northern part of Karnataka, and was once the capital of the Vijayanagara Empire. The ruins of Hampi are spread across a vast area, and include temples, palaces, and other structures that give visitors a glimpse into the rich history and culture of the region. The most famous attractions in Hampi include the Virupaksha Temple, the Vittala Temple, and the Hampi Bazaar.' ,'url':'https://4.bp.blogspot.com/-6ICyHR61RF0/Tobw5CFOjwI/AAAAAAAAATk/tJng4rR2ov8/s1600/hampi+%25281%2529.jpg'},
        {'place': 'Gokarna Beach','long':14.533770, 'lat':74.317370 ,'temp':24 , 'type': 'Beach','details':'Gokarna Beach: This picturesque beach town is located on the western coast of Karnataka, and is known for its stunning beaches and relaxed atmosphere. The most popular beach in Gokarna is Om Beach, which is named after its distinctive shape that resembles the Hindu symbol for Om. Other popular beaches in the area include Kudle Beach, Half Moon Beach, and Paradise Beach.' ,'url':'https://images.thrillophilia.com/image/upload/s--uDJGhoiH--/c_fill,g_auto/v1/attractions/images/000/002/841/original/Om-Beach-2.jpg.jpg'},
        {'place': 'Dubare Elephant Camp','long':12.368530, 'lat':75.904907 ,'temp':24 , 'type': 'Wildlife','details':'Dubare Elephant Camp: This wildlife sanctuary is located near the town of Kushalnagar in Karnataka, and is home to a large population of elephants. Visitors to the camp can participate in activities such as elephant rides, elephant bathing, and feeding the elephants. The camp also offers opportunities for bird watching and hiking in the surrounding forests.' ,'url':'https://www.explorebees.com/uploads/Dubare%20Elephant%20Camp.jpg'},
        {'place': 'Chikmagalur','long':13.312320, 'lat':75.770890 ,'temp':24 , 'type': 'Hill Station','details':'Chikmagalur: This hill station is located in the western part of Karnataka, and is known for its stunning natural beauty and coffee plantations. Visitors to Chikmagalur can enjoy activities such as trekking, camping, and bird watching, as well as visiting the many coffee estates in the area. The most popular attractions in Chikmagalur include the Mullayanagiri Peak, the Bhadra Wildlife Sanctuary, and the Hebbe Falls.' ,'url':'https://img.cdn.zostel.com/blog_photo/21688469_856109361224117_4637377196186256857_o.jpg'},
        ],

    'Kerala': [
        {'place': 'Backwaters of Kerala','long':9.655677, 'lat':76.384140 , 'temp':24 ,'type': 'Scenic','details':'Backwaters of Kerala: The backwaters of Kerala are a network of interconnected canals, lagoons, and lakes that lie parallel to the Arabian Sea coast. It is a scenic destination and a popular tourist attraction in Kerala. Visitors can explore the backwaters by taking a houseboat ride or a canoe ride. Some of the popular backwater destinations in Kerala include Alleppey, Kumarakom, and Kollam.' ,'url':'https://www.tripsavvy.com/thmb/P-vBKShJXcsDT_5m-IF2xSMQ8q0=/3600x2400/filters:fill(auto,1)/GettyImages-522478216-5ab12c4e3de4230036949cee.jpg'},
        {'place': 'Athirappilly Falls','long':10.287101,'lat': 76.570152 ,'temp':24 , 'type': 'Scenic','details':'Athirappilly Falls: Located in Thrissur district of Kerala, Athirappilly Falls is a scenic waterfall that cascades down from a height of 80 feet. The waterfall is surrounded by lush green forests and is a popular destination for nature lovers and adventure enthusiasts. Visitors can take a trek to the waterfall and enjoy the beautiful views from the top.' ,'url':'https://www.tripsavvy.com/thmb/0iJ8frKC6uDjRvon3RiR-k3DWU4=/3008x2000/filters:fill(auto,1)/GettyImages-141296615-aafce3a8534c45aba8afd312fa155cea.jpg'},
        {'place': 'Hill Palace','long':9.952496, 'lat':76.364323 ,'temp':24 , 'type': 'Historical','details':'Hill Palace: Located in Tripunithura, Hill Palace is the largest archaeological museum in Kerala. It was the official residence of the Kochi royal family and is now a museum that showcases their art, artifacts, and history. The museum has a vast collection of paintings, sculptures, manuscripts, and coins.' ,'url':'https://4.bp.blogspot.com/-XT0of2h4f2c/V2aYSZdFdtI/AAAAAAAAJBg/gJHUSObF2soMk9uW6d7e-h2ggp4Djz2FgCLcB/s1600/IMG_3215.JPG'},
        {'place': 'Fort Kochi','long':9.968000, 'lat':76.244000 ,'temp':24 , 'type': 'Historical','details':'Fort Kochi: Fort Kochi is a historic neighborhood in Kochi that has a mix of Portuguese, Dutch, and British colonial architecture. The area is known for its charming streets, spice markets, and seafood restaurants. Some of the popular attractions in Fort Kochi include the Chinese fishing nets, St. Francis Church, and the Mattancherry Palace.' ,'url':'https://www.tripsavvy.com/thmb/rRC9tDpbSg-h_ETu0nOpzphYI8k=/2122x1415/filters:fill(auto,1)/GettyImages-148935094-583dbb6e5f9b58d5b129a27c.jpg'},
        {'place': 'Kovalam Beach','long':8.383229, 'lat':76.983570 ,'temp':24 , 'type': 'Beach','details':'Kovalam Beach: Kovalam Beach is a popular beach destination in Kerala. The beach is known for its soft sand, clear waters, and scenic beauty. Visitors can indulge in various activities like swimming, surfing, and sunbathing. The beach also has several restaurants and cafes that serve delicious seafood and other local delicacies.' ,'url':'https://static.toiimg.com/photo/66971666/kovalam-lighthouse.jpg?width=748&resize=4'},
        ],

    'Madhya Pradesh': [
        {'place': 'Khajuraho Temples','long':24.853411, 'lat':79.919708 ,'temp':24 , 'type': 'Historical','details':'Khajuraho Temples: These temples are known for their stunning architecture and intricate carvings depicting various scenes of human life. They were built during the Chandela dynasty between 950 and 1050 AD. There are 20 temples in total, out of which the most famous ones are the Kandariya Mahadeva Temple, Chausath Yogini Temple, and Lakshmana Temple.' ,'url':'https://www.tripsavvy.com/thmb/m0UXW7btnS100RvrmI35bfOYWwg=/3000x2000/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-540115304-c91172725e8143898e263a3500b19d39.jpg'},
        {'place': 'Sanchi Stupa','long':23.480690, 'lat':77.736382 , 'temp':24 ,'type': 'Historical','details':'Sanchi Stupa: Sanchi Stupa is a Buddhist complex located in Sanchi, Madhya Pradesh. It is famous for its Great Stupa, which was built by Emperor Ashoka in the 3rd century BC. The Stupa is a UNESCO World Heritage Site and is one of the oldest stone structures in India.' ,'url':'https://www.tripsavvy.com/thmb/v3v4i4F5IxzrtJTol5lGq8xHwRQ=/4256x2832/filters:fill(auto,1)/GettyImages-884038548-5c6ac51546e0fb0001f0e4cf.jpg'},
        {'place': 'Bandhavgarh National Park','long':23.722454, 'lat':81.024246 , 'temp':24 ,'type': 'Wildlife','details':'Bandhavgarh National Park: This national park is located in the Umaria district of Madhya Pradesh. It is famous for its high density of Bengal tigers, as well as other wildlife like leopards, wild boars, and Indian bison. The park also has several ancient caves and rock shelters with inscriptions and carvings.' ,'url':'https://th.bing.com/th/id/R.d682645a58cd8fbf13de8e2e13460cf2?rik=mhSTiulwcI3moA&riu=http%3a%2f%2fbooklikes.com%2fupload%2fpost%2fd%2f6%2fd682645a58cd8fbf13de8e2e13460cf2.jpg&ehk=oHMNiEtiTTuA2AyCbfdbV9gs4oGuZFMnN0ehkqLYViE%3d&risl=&pid=ImgRaw&r=0'},
        {'place': 'Bhedaghat Marble Rocks','long':23.130810, 'lat':79.801930 ,'temp':24 , 'type': 'Scenic','details':'Bhedaghat Marble Rocks: These are white marble cliffs rising on either side of the Narmada River. The marble has been eroded by the river over millions of years, creating stunning natural formations. The best time to visit is during the monsoon season when the river is full and the waterfalls are in full flow.' ,'url':'https://th.bing.com/th/id/R.5e74fbaeacb7b6a1ee4ac83e8642d0a2?rik=9S9U0UXX%2bVGC%2bg&riu=http%3a%2f%2fwww.visitindia.org.in%2fmadhya+pradesh%2fimages%2fWhite_Marble_Rocks_at_Bhedaghat.jpg&ehk=32NSGbm6%2bHYAMLWwQpxmx2z8ai%2f2Kl8ZWF1CwlbSRIk%3d&risl=&pid=ImgRaw&r=0'},
        {'place': 'Pachmarhi Hill Station','long':22.466100, 'lat':78.427100 , 'temp':24 ,'type': 'Hill Station','details':'Pachmarhi Hill Station: Pachmarhi is a popular hill station located in the Satpura Range. It is known for its scenic beauty, waterfalls, and ancient caves. Some popular tourist spots include the Bee Falls, Jata Shankar Caves, and Rajat Prapat waterfall.' ,'url':'https://i.pinimg.com/736x/55/2b/84/552b84952a1199832d0591583d778d33--madhya-pradesh-one-and-only.jpg'},
        ],

    'Maharashtra': [
        {'place': 'Gateway of India','long':18.921970, 'lat':72.834557 ,'temp':24 , 'type': 'Historical','details':'Gateway of India: The Gateway of India is an arch monument built during the 20th century in Mumbai. It was built to commemorate the visit of King George V and Queen Mary to Mumbai. The monument has historical significance as it was the point of entry for British viceroys and governors who visited India. It is also a popular tourist spot and offers a stunning view of the Arabian Sea.' ,'url':'https://im.whatshot.in/img/2019/Feb/gateway-of-india-4b-cropped-1549871701.jpg'},
        {'place': 'Ajanta and Ellora Caves','long':20.021170,'lat': 75.179573 , 'temp':24 ,'type': 'Historical','details':'Ajanta and Ellora Caves: The Ajanta and Ellora Caves are a group of rock-cut caves in Maharashtra, India. They are renowned for their historical and archaeological significance as well as their architectural beauty. The caves contain ancient Buddhist, Jain, and Hindu temples and monasteries that were built between the 2nd century BC and the 6th century AD. The caves are a UNESCO World Heritage Site.' ,'url':'https://www.tripsavvy.com/thmb/Ixa2ct8tovqLtIkkVvycgLtK4nk=/5902x3957/filters:fill(auto,1)/AjantaCaves-India-AnnaHaines127-8a5d29273ba34eb4a938557b9a10b2e3.jpg'},
        {'place': 'Siddhivinayak Temple','long':19.017946, 'lat':72.831757 ,'temp':24 , 'type': 'Religious','details':'Siddhivinayak Temple: The Siddhivinayak Temple is a Hindu temple dedicated to Lord Ganesha, located in Mumbai. It is one of the most famous and popular temples in Mumbai, attracting thousands of devotees every day. The temple was built in 1801 and is known for its beautiful architecture and intricate carvings.' ,'url':'https://th.bing.com/th/id/R.192aac5bab66c0c3deeaa333b79be742?rik=7SaPLImWj%2fnL5A&riu=http%3a%2f%2f1.bp.blogspot.com%2f-t_kWPbnUZkI%2fUodnfCB1XfI%2fAAAAAAAAED8%2fNVbc2nvciXc%2fs1600%2fshree_siddhivinayak_temple_mumbai.jpg&ehk=rDmuDPW4SWlAUZta5OETtGLdzYTbguuYy5YPL8mb%2fxA%3d&risl=&pid=ImgRaw&r=0'},
        {'place': 'Lonavala Hill Station','long':18.749331, 'lat':73.408028 , 'temp':24 ,'type': 'Hill Station','details':'Lonavala Hill Station: Lonavala is a beautiful hill station located in the Western Ghats of Maharashtra. It is a popular weekend getaway for people living in Mumbai and Pune. The hill station is known for its scenic beauty, lush green valleys, and waterfalls. The place also offers adventure activities like trekking, camping, and rappelling.' ,'url':'https://www.unexplora.com/wp-content/uploads/2018/04/Mumbai-Lonavala.jpg'},
        {'place': 'Elephanta Caves','long':18.921989, 'lat':72.834541 ,'temp':24 , 'type': 'Historical','details':'Elephanta Caves: The Elephanta Caves are a group of rock-cut caves located on the Elephanta Island in Mumbai. The caves contain ancient Hindu and Buddhist temples and sculptures that date back to the 5th century. The caves are a UNESCO World Heritage Site and are considered to be one of the finest examples of Indian rock-cut architecture.' ,'url':'https://www.mumbailive.com/images/media/images/images_1550743375105_ashwin_kumar_flickr.jpg'},
        ],

    'Manipur': [
        {'place': 'Loktak Lake','long':24.554260, 'lat':93.812584 ,'temp':24 , 'type': 'Scenic','details':'Loktak Lake: This is the largest freshwater lake in Northeast India and is located in Manipur. It is known for its floating islands called phumdis, which are made up of vegetation and organic matter. Visitors can take a boat ride to explore the lake and its surroundings, and also visit the Keibul Lamjao National Park which is located within the lake.' ,'url':'https://th.bing.com/th/id/R.9cad8733f08b46eb507025d723d20a40?rik=UkBWKzvQg2pehQ&riu=http%3a%2f%2fwww.lostwithpurpose.com%2fwp-content%2fuploads%2f2017%2f07%2fDSC07518.jpg&ehk=IJM1mKj8%2bpDsWqoqtj5Bo%2bP2SyxGFhLJzZ%2flSzYmkdQ%3d&risl=&pid=ImgRaw&r=0'},
        {'place': 'Manipur State Museum','long':24.803499, 'lat':93.941544 ,'temp':24 , 'type': 'Museum','details':'Manipur State Museum: This museum is located in Imphal and has a collection of artifacts related to the history and culture of Manipur. Some of the exhibits include ancient manuscripts, traditional costumes, weapons, and musical instruments.' ,'url':'https://images.herzindagi.info/image/2019/Nov/manipur-state-museum.jpg'},
        {'place': 'Sirohi National Park','long':24.230829, 'lat':94.230827 , 'temp':24 ,'type': 'Wildlife','details':'Sirohi National Park: This national park is located in Manipur and is home to a variety of wildlife such as deer, leopards, and hoolock gibbons. Visitors can go on a jungle safari to explore the park and its flora and fauna.' ,'url':'https://www.trodly.com/pictures/attraction/6122.jpg'},
        {'place': 'Kaina Hill Station','long':24.230829, 'lat':94.230827 , 'temp':24 ,'type': 'Hill Station','details':'Kaina Hill Station: This hill station is located in Manipur and is known for its scenic beauty and pleasant weather. Visitors can enjoy activities such as trekking, camping, and birdwatching, and also visit the nearby Kaina Temple which is dedicated to Lord Krishna.' ,'url':'https://www.travelplaceindia.com/wp-content/uploads/2019/11/2016_txindoki_ekaina_006.jpg'},
        ],

    'Meghalaya': [
        {'place': 'Living Root Bridges','long':25.178030,'lat': 91.744720 ,'temp':24 , 'type': 'Nature','details':'Living Root Bridges: Located in the southern part of Meghalaya, Living Root Bridges are a unique natural wonder where bridges are formed by the roots of trees. These bridges are hand-crafted by the Khasi and Jaintia tribes using the roots of Ficus elastica trees. The most famous of these bridges is the Double Decker Living Root Bridge, which is located in the village of Nongriat and is around 150 years old. Visitors can trek through lush green forests to reach the bridges and witness the amazing natural engineering at work.' ,'url':'https://i1.wp.com/hyperallergic.com/wp-content/uploads/2017/07/living-root-bridges-home.jpg?fit=1000%2C618&quality=100&ssl=1'},
        {'place': 'Nohkalikai Falls','long':25.275677,'lat': 91.686974 ,'temp':24 , 'type': 'Waterfall','details':'Nohkalikai Falls: Located near Cherrapunji, Nohkalikai Falls is one of the tallest waterfalls in India, with a height of around 340 meters. The waterfall is named after a tragic legend involving a woman named Likai, whose husband killed and cooked their daughter, leading her to jump off the cliff near the waterfall. Visitors can witness the majestic falls and take in the stunning views of the surrounding hills and valleys.' ,'url':'https://i.pinimg.com/originals/cf/db/98/cfdb9824f74e0b64b28022b5af2d0627.jpg'},
        {'place': 'Elephant Falls','long':25.537512, 'lat':91.822189 ,'temp':24 , 'type': 'Waterfall','details':'Elephant Falls: Located near Shillong, Elephant Falls is a three-tiered waterfall that cascades down through lush greenery. The name "Elephant Falls" is derived from a rock near the falls that is said to resemble an elephant. Visitors can take a short hike down to the falls and witness the beauty of the cascading water.' ,'url':'https://th.bing.com/th/id/OIP.ZAyd0-ivt1akgV1Ma7D6RwHaEv?w=304&h=195&c=7&r=0&o=5&dpr=1.3&pid=1.7'},
        {'place': 'Shillong Peak','long':25.547432, 'lat':91.874992 ,'temp':24 , 'type': 'Mountain','details':'Shillong Peak: Located around 10 kilometers from Shillong, Shillong Peak is the highest point in the city at an altitude of 1,965 meters. Visitors can drive up to the peak and take in panoramic views of the city and surrounding hills. On a clear day, the peak offers stunning views of the Himalayas.' ,'url':'https://c1.staticflickr.com/4/3687/10340338253_1e866e24cd_b.jpg'},
        {'place': 'Mawphlang Sacred Grove','long':25.452360, 'lat':91.753250 ,'temp':24 , 'type': 'Nature','details':'Mawphlang Sacred Grove: Located around 25 kilometers from Shillong, Mawphlang Sacred Grove is a dense forest that is considered sacred by the Khasi tribe. The forest is home to a variety of flora and fauna, including many rare and endangered species. Visitors can take a guided tour through the forest and learn about the cultural and ecological significance of the grove.' ,'url':'https://th.bing.com/th/id/OIP.uu460kifjaEwCwUAAOyySQHaEt?w=302&h=192&c=7&r=0&o=5&dpr=1.3&pid=1.7'},
        ],
    'Mizoram': [
        {'place': 'Phawngpui National Park','long':22.741261, 'lat':93.096428 ,'temp':24 , 'type': 'Nature','details':'Phawngpui National Park: Located in the southern part of Mizoram, Phawngpui National Park is a popular destination for nature lovers and trekkers. The park is home to a variety of flora and fauna, including the red panda, hoolock gibbon, and various species of birds. The park also has several trekking trails that offer panoramic views of the surrounding hills and valleys.' ,'url':'https://www.hlimg.com/images/things2do/738X538/ttd_1522922804m4.jpg'},
        {'place': 'Murlen National Park','long':23.994211, 'lat':93.219208 ,'temp':24 , 'type': 'Nature','details':'Murlen National Park: Situated in the Champhai district of Mizoram, Murlen National Park is known for its rich biodiversity and scenic beauty. The park is home to several species of animals, including the Himalayan black bear, serow, and barking deer. It also has several trekking trails that offer stunning views of the surrounding hills and valleys. ' ,'url':'https://static2.tripoto.com/media/filter/tst/img/7372/TripDocument/1510641503_champhai.jpg'},
        {'place': 'Durtlang Hills','long':23.774040, 'lat':92.726097 , 'temp':24 ,'type': 'Mountain','details':'Durtlang Hills: Located on the outskirts of Aizawl, Durtlang Hills is a popular destination for nature lovers and adventure enthusiasts. The hills offer panoramic views of the city and are a great place for hiking and trekking.' ,'url':'https://www.hlimg.com/images/things2do/738X538/Durtlang_Hills_vc4t9e_1523006453t.jpg'},
        {'place': 'Reiek Village','long':23.678000, 'lat':92.603000 ,'temp':24 , 'type': 'Village','details':'Reiek Village: Situated at a distance of about 29 km from Aizawl, Reiek Village is a popular tourist destination in Mizoram. The village is known for its scenic beauty and is surrounded by lush green hills. It also has several trekking trails that offer stunning views of the surrounding landscape.' ,'url':'https://www.scrolldroll.com/wp-content/uploads/2018/05/Reiek-Heritage-Village-Mizoram-Places-To-Visit-In-North-East.jpg'},
        {'place': 'Aizawl Museum','long':23.738140, 'lat':92.715790 ,'temp':24 , 'type': 'Museum','details':'Aizawl Museum: Located in the heart of Aizawl, the Aizawl Museum is a must-visit destination for history and culture enthusiasts. The museum showcases the rich cultural heritage of Mizoram, with exhibits on art, history, and traditional costumes and handicrafts.' ,'url':'https://th.bing.com/th/id/R.29cfb897faa5af5cb8881136f812b5b0?rik=7aDCxcGfWaaGpw&riu=http%3a%2f%2fwww.wanderglobe.org%2fwp-content%2fuploads%2f2017%2f10%2fMizoram-State-Museum.jpg&ehk=kEN7wzKp5TQKc%2ftyNkxo9IDUcMyfevR8HEdDoNeZ25c%3d&risl=&pid=ImgRaw&r=0'},
        ],
    'Nagaland': [
        {'place': 'Dzukou Valley','long':25.553480, 'lat':94.067020 ,'temp':24 , 'type': 'Nature','details':'Dzukou Valley: Located on the border of Nagaland and Manipur, Dzukou Valley is known for its lush greenery, rolling hills, and beautiful flowers. The valley is a popular trekking destination and offers breathtaking views of the surrounding landscape.' ,'url':'https://blog.kitemanja.com/wp-content/uploads/2018/05/dzukou-valley-image-1024x681.jpg'},
        {'place': 'Naga Heritage Village','long':25.616529, 'lat':94.114113 ,'temp':24 , 'type': 'Village','details':'Naga Heritage Village: Located in Kisama, near Kohima, the Naga Heritage Village is a living museum that showcases the traditional way of life of the Naga tribes. The village features various traditional Naga houses, crafts, and artifacts.' ,'url':'https://www.esamskriti.com/photograph/79_2488.jpg?202011281219'},
        {'place': 'Triple Falls','long':25.919831,'lat': 94.479332 ,'temp':24 , 'type': 'Waterfall','details':'Triple Falls: Located near Seithekima Village in Dimapur district, Triple Falls is a beautiful waterfall that is formed by the Dzü River. The waterfall is surrounded by lush green forests and is a popular picnic spot.' ,'url':'https://www.connectingtraveller.com/images/localtip/16543372051583006415_shutterstock_1416649112.jpg.jpg'},
        {'place': 'Intanki Wildlife Sanctuary','long':25.549173, 'lat':93.519897 ,'temp':24 , 'type': 'Wildlife','details':'Intanki Wildlife Sanctuary: Located in the Peren district, the Intanki Wildlife Sanctuary is home to a variety of wildlife, including tigers, elephants, leopards, and bears. The sanctuary also features a diverse range of flora and fauna.' ,'url':'https://www.travelplanet.in/wp-content/uploads/2018/10/Intanki-Wildlife-Sanctuary-source-KHBUZZ.jpg'},
        ],
    'Odisha': [
        {'place': 'Konark Sun Temple','long':19.887621,'lat':86.094543 ,'temp':24 , 'type': 'Historical','details':'Konark Sun Temple: Located in the eastern state of Odisha, the Konark Sun Temple is a UNESCO World Heritage Site and is famous for its impressive architecture and intricate carvings. It was built in the 13th century in the shape of a chariot with 12 wheels, pulled by seven horses. The temple is dedicated to the Sun God and is one of the most popular tourist destinations in Odisha.' ,'url':'https://th.bing.com/th/id/OIP.cAkA1fXWyKT90MK5zclRVgHaFj?pid=ImgDet&rs=1'},
        {'place': 'Jagannath Temple','long':19.804699,'lat':85.818153 ,'temp':24 , 'type': 'Religious','details':'Jagannath Temple: Another popular religious site in Odisha is the Jagannath Temple, located in the city of Puri. The temple is dedicated to Lord Jagannath, a form of Lord Vishnu, and is one of the Char Dham pilgrimage sites for Hindus. The temple is famous for its annual Rath Yatra or Chariot Festival, which attracts millions of devotees from all over India.' ,'url':'https://static.toiimg.com/photo/64589480/jagannath-2.jpg?width=748&resize=4'},
        {'place': 'Chilika Lake','long':19.706229,'lat': 85.322941 , 'temp':24 ,'type': 'Lake','details':'Chilika Lake: Chilika Lake is a brackish water lagoon located in the eastern state of Odisha. It is the largest coastal lagoon in India and is a popular tourist destination known for its biodiversity and scenic beauty. The lake is home to a variety of migratory birds, including flamingos, and is also a major fishing zone.' ,'url':'https://thumbs.dreamstime.com/b/chilika-lake-brackish-water-lagoon-spread-over-puri-khurda-ganjam-districts-odisha-state-east-coast-india-147817009.jpg'},
        {'place': 'Dhauli Hill','long':20.219639,'lat':85.862083 , 'temp':24 ,'type': 'Historical','details':'Dhauli Hill: Dhauli Hill is a hill located on the banks of the Daya River in Odisha. It is famous for its rock edicts, which were inscribed by Emperor Ashoka in the 3rd century BCE. The edicts promote peace and non-violence and are considered an important historical and cultural site in India.' ,'url':'https://i.pinimg.com/originals/d3/b9/76/d3b9769959ee77986825c19c66fe4c92.jpg'},
        {'place': 'Puri Beach','long':19.789919,'lat':85.806709 ,'temp':24 , 'type': 'Beach','details':'Puri Beach: Puri Beach is a popular beach located in the city of Puri in Odisha. It is known for its golden sand, clear blue waters, and lively atmosphere. The beach is a popular destination for swimming, sunbathing, and surfing, and is also home to a number of seafood shacks and souvenir shops.' ,'url':'https://imgcld.yatra.com/ytimages/image/upload/v1434961689/Beach_Puri.jpg'},
        ],
    'Punjab': [
        {'place': 'Golden Temple','long':31.619989,'lat':74.876534 ,'temp':24 , 'type': 'Religious','details':'Golden Temple: The Golden Temple, also known as Sri Harmandir Sahib, is a revered Sikh gurudwara located in the city of Amritsar, Punjab. It is considered to be one of the holiest places in Sikhism and attracts millions of visitors every year. The temple complex is made of white marble and is topped with a dome covered in gold foil, giving it its iconic appearance. Visitors can take a dip in the holy water pool inside the complex, listen to the recitation of the Guru Granth Sahib (the Sikh holy scripture), and partake in the langar (free community meal) that is served daily.' ,'url':'https://1.bp.blogspot.com/-SwoB_RpA3-k/VB7bqoIEz0I/AAAAAAAASJ8/xs_5pCLrL3c/s1600/amritsar+golden+temple+morning1.jpg'},
        {'place': 'Wagah Border','long':31.604720,'lat': 74.573060 ,'temp':24 , 'type': 'Historical','details':'Wagah Border: The Wagah Border is a border crossing between India and Pakistan, located near the city of Amritsar in Punjab. It is known for the daily ceremonial border closing ceremony that takes place in the evenings, where soldiers from both countries perform a coordinated parade and flag-lowering ceremony. Visitors can witness this spectacle from designated viewing areas on either side of the border.' ,'url':'https://api.time.com/wp-content/uploads/2014/11/india_pakistan_wagah_border.jpg'},
        {'place': 'Jallianwala Bagh','long':31.620331,'lat':74.879593 , 'temp':24 ,'type': 'Historical','details':'Wagah Border: The Wagah Border is a border crossing between India and Pakistan, located near the city of Amritsar in Punjab. It is known for the daily ceremonial border closing ceremony that takes place in the evenings, where soldiers from both countries perform a coordinated parade and flag-lowering ceremony. Visitors can witness this spectacle from designated viewing areas on either side of the border.' ,'url':'https://static.toiimg.com/photo/68860078.cms'},
        {'place': 'Akal Takht','long':31.620630,'lat': 74.875420 , 'temp':24 ,'type': 'Religious','details':'Akal Takht: Akal Takht is one of the five Takhts (holy seats) of Sikhism, located in the city of Amritsar, Punjab. It is the highest temporal seat of Sikhism and is considered the central governing authority of the religion. The Akal Takht is also the site of the Sikh Parliament, where issues related to the religion and community are discussed and decisions are made.' ,'url':'https://th.bing.com/th/id/R.3e00011e15650a99e84a901977ee315a?rik=A7kHkHdsXigVEQ&riu=http%3a%2f%2fppcdn.500px.org%2f50020424%2f2abeddedd930c60dfe7e749ab9318a27cfad1c93%2f2048.jpg&ehk=tEtR0Sl3Y9s39zT3eqfs7Pfu7fR%2fZz6O9Rp8eYK2MlI%3d&risl=&pid=ImgRaw&r=0'},
        {'place': 'Anandpur Sahib','long':31.239090,'lat':76.536452 ,'temp':24 , 'type': 'Religious','details':'Anandpur Sahib: Anandpur Sahib is a city located in the Rupnagar district of Punjab and is considered one of the holiest places in Sikhism. It is home to several gurudwaras and is the birthplace of the Khalsa, the community of baptized Sikhs. The city is also known for the Hola Mohalla festival, which is celebrated annually and involves martial arts displays and other cultural events' ,'url':'https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/2_Sri_Kesgarh_Takhat_Anandpur_Sahib_Khalsa_birthplace_Himalayan_foothills_in_view_Punjab_India.jpg/1200px-2_Sri_Kesgarh_Takhat_Anandpur_Sahib_Khalsa_birthplace_Himalayan_foothills_in_view_Punjab_India.jpg'},
        ],
    'Rajasthan': [
        {'place': 'Hawa Mahal','long':26.923990,'lat':75.826668 ,'temp':28 , 'type': 'Historical','details':'Hawa Mahal: Located in the heart of Jaipur, Hawa Mahal is a stunning five-story palace with 953 small windows known as jharokhas.It was built in 1799 by Maharaja Sawai Pratap Singh to allow the royal ladies to observe daily life and festivals in the street below without being seen themselves.' ,'url':'https://th.bing.com/th/id/OIP.rCrmD4v8wkEq2knJwOxzWwHaFN?pid=ImgDet&rs=1'},
        {'place': 'City Palace Jaipur','long':26.925779,'lat':75.823647 ,'temp':28 , 'type': 'Historical','details':'City Palace Jaipur: Another beautiful palace located in Jaipur, City Palace was built by Maharaja Sawai Jai Singh II in the 18th century. The palace complex includes several buildings and courtyards with impressive architecture and design, reflecting a blend of Rajasthani and Mughal styles.' ,'url':'https://images.thrillophilia.com/image/upload/s--5fZFSNo9--/c_fill,g_auto/v1/attractions/images/000/004/385/original/1605795365_shutterstock_197923865.jpg.jpg'},
        {'place': 'Amber Fort','long':26.985498,'lat':75.851349 ,'temp':24 , 'type': 'Historical','details':'Amber Fort: Located just outside Jaipur, Amber Fort is a magnificent fortress built by Raja Man Singh I in the 16th century. The fort is made of yellow and pink sandstone and marble and features several beautiful palaces, temples, and gardens within its walls.' ,'url':'https://www.tripsavvy.com/thmb/iVN0yWFtZwLwKwSXARuvmNh3U_4=/3311x2216/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-524151419-6d874058218e48e88803c5fca2f6c1d2.jpg'},
        {'place': 'Thar Desert','long':27.914920,'lat': 72.847230 ,'temp':24 , 'type': 'Desert','details':'Thar Desert: The Thar Desert is a vast, arid region located in the northwestern part of India, covering parts of Rajasthan and Gujarat. It is known for its stunning sand dunes, camel safaris, and beautiful sunsets.' ,'url':'https://budgetindiantraveler.co.in/wp-content/uploads/2019/02/thar.jpg'},
        {'place': 'Lake Palace','long':24.575070,'lat':73.680220 ,'temp':24 , 'type': 'Palace','details':'Lake Palace: A former royal palace located in Udaipur, Lake Palace is a stunning white marble palace situated on an island in Lake Pichola. Built-in 1746, the palace now operates as a luxury hotel and is a popular tourist attraction.' ,'url':'https://www.travelplusstyle.com/wp-content/gallery/taj-lake-palace-udaipur/taj_lake_palace_hotel_1-b.jpg'},
        ],
    'Sikkim': [
        {'place': 'Nathula Pass','long':27.386845,'lat':88.831139 ,'temp':19 , 'type': 'Mountain','details':'Nathula Pass: It is a mountain pass located on the Indo-China border and is one of the highest motorable roads in the world. The pass is surrounded by snow-covered mountains and offers breathtaking views of the Himalayas.' ,'url':'https://nomadicweekends.com/blog/wp-content/uploads/2019/03/Road-to-Nathula-Pass.jpg'},
        {'place': 'Tsomgo Lake','long':27.375280,'lat':88.763893 , 'temp':19 ,'type': 'Lake','details':'Tsomgo Lake: It is a glacial lake located at an altitude of 12,400 feet and is a popular tourist destination in Sikkim. The lake is surrounded by snow-capped mountains and is considered sacred by the locals.' ,'url':'https://www.adotrip.com/public/images/areas/5c3f0ab44a055-Tsomgo_Lake_Package_Tour.jpg'},
        {'place': 'Rumtek Monastery','long':27.288691,'lat': 88.561462 ,'temp':22 , 'type': 'Religious','details':'Rumtek Monastery: It is a Tibetan Buddhist monastery located in the capital city of Gangtok. The monastery is known for its exquisite architecture and is one of the largest monasteries in Sikkim.' ,'url':'https://static.toiimg.com/photo/msid-56621729,width-96,height-65.cms'},
        {'place': 'Goecha La Trek','long':27.607780,'lat':88.186940 , 'temp':15 ,'type': 'Trekking','details':'Goecha La Trek: It is a trekking trail that takes you to the base of the Kanchenjunga peak, the third-highest mountain in the world. The trek offers stunning views of the mountains and the surrounding landscape.' ,'url':'https://ridingsolo.in/blog/wp-content/uploads/2019/11/Trek2.jpg-1.jpg'},
        {'place': 'Kanchenjunga National Park','long':27.667345,'lat':88.324585 , 'temp':24 ,'type': 'Wildlife','details':'Kanchenjunga National Park: It is a UNESCO World Heritage Site and a biodiversity hotspot located in the Himalayan range. The park is home to several endangered species of flora and fauna, including the snow leopard, red panda, and Himalayan black bear.' ,'url':'https://www.trawell.in/admin/images/upload/723415851Gangtok_Kanchendzonga_National_Park_Main.jpg'},
        ],
    'Tamil Nadu': [
        {'place': 'Meenakshi Temple','long':9.919504,'lat':78.119339 ,'temp':33 , 'type': 'Religious','details':'Meenakshi Temple: Located in the city of Madurai in Tamil Nadu, this temple is dedicated to Goddess Meenakshi, a form of Parvati. It is known for its intricate carvings and is a popular pilgrimage site for Hindus. The temple complex also includes a number of smaller shrines and a tank. The temperature in Madurai in May ranges from 28-35 degrees Celsius.' ,'url':'https://th.bing.com/th/id/R.2d22cd97f40071e2859a4eac722bf9c8?rik=woB5Z%2fzAUvs1lQ&riu=http%3a%2f%2f2.bp.blogspot.com%2f-Y5Lss7-vmCg%2fU8KqUDKzP9I%2fAAAAAAAAR8s%2fbafexw-8KWY%2fs1600%2fMeenakshi%2bTemple%2b(1).jpg&ehk=NWQfPeaL1jRUWMIuDrzEx21T8zfTFGYDXzdsG%2feogXg%3d&risl=&pid=ImgRaw&r=0'},
        {'place': 'Marina Beach','long':13.051910,'lat':80.282898 , 'temp':35 ,'type': 'Beach','details':'Marina Beach: This is a popular beach located in Chennai, the capital city of Tamil Nadu. It is one of the longest urban beaches in the world, stretching over 13 kilometers. Visitors can enjoy a variety of activities like swimming, beach volleyball, and horse riding. The temperature in Chennai in May ranges from 28-35 degrees Celsius.' ,'url':'https://imgcld.yatra.com/ytimages/image/upload/v1437483460/Marina_Beach.jpg'},
        {'place': 'Mahabalipuram','long':12.614490,'lat':80.166500 ,'temp':34 , 'type': 'Historical','details':'Mahabalipuram: Located about 60 kilometers from Chennai, Mahabalipuram is a UNESCO World Heritage Site and is known for its ancient temples and rock-cut sculptures. The Shore Temple, dedicated to Lord Shiva, is a popular attraction here. The temperature in Mahabalipuram in May ranges from 28-35 degrees Celsius.' ,'url':'https://cdn.audleytravel.com/4536/3240/79/208939-shore-temple-mahabalipuram-india.jpg'},
        {'place': 'Ooty','long':11.411750,'lat':76.694660 , 'temp':17 ,'type': 'Hill Station','details':'Ooty: Also known as Udhagamandalam, Ooty is a hill station located in the Nilgiri Hills of Tamil Nadu. It is known for its scenic beauty and cool weather. Visitors can enjoy activities like trekking, boating, and visiting tea estates. The temperature in Ooty in May ranges from 15-22 degrees Celsius.' ,'url':'https://experiencekerala.in/image-uploads/1468473509.Ooty_Lake.jpg'},
        {'place': 'Madurai','long':9.924000,'lat':78.123960 ,'temp':34 , 'type': 'Historical','details':'Madurai: Madurai is an ancient city in Tamil Nadu and is known for its rich cultural heritage. It is home to the Meenakshi Temple and many other historical monuments like the Thirumalai Nayakkar Palace and the Gandhi Memorial Museum. The temperature in Madurai in May ranges from 28-35 degrees Celsius.' ,'url':'https://upload.wikimedia.org/wikipedia/commons/b/b5/India_-_Madurai_temple_-_0781.jpg'},
        ],
    'Telangana': [
        {'place': 'Ramoji Film City','long':17.245160,'lat':78.680960 ,'temp':31 , 'type': 'Entertainment','details':'Ramoji Film City: A film studio complex and tourist attraction located in Hyderabad. It is one of the largest film cities in the world and offers film-themed tours, shows, and rides.' ,'url':'https://buddymantra.com/wp-content/uploads/2018/01/ramoji-film-city.jpg'},
        {'place': 'Warangal Fort','long':17.956160,'lat':79.614693 ,'temp':30 , 'type': 'Historical','details':'Warangal Fort: A 13th-century fort located in Warangal, Telangana. It was the capital of the Kakatiya dynasty and has architectural features such as the Thousand Pillar Temple and the Ramappa Temple.' ,'url':'https://www.thetoptours.com/wp-content/uploads/warangal-fort-scaled.jpg'},
        {'place': 'Salar Jung Museum','long':17.371250,'lat':78.480377 , 'temp':31 ,'type': 'Museum','details':'Salar Jung Museum: A museum located in Hyderabad, known for its collection of art, sculptures, and artifacts from around the world. It has over one million objects and is one of the largest museums in India.' ,'url':'https://www.coveringindia.com/resources/fullsize/salar-jung-museum-main-873.jpg'},
        {'place': 'Golconda Fort','long':17.383310,'lat': 78.401047 ,'temp':32 , 'type': 'Historical','details':'Golconda Fort: A 16th-century fort located in Hyderabad, known for its impressive architecture and engineering. It has a sound and light show in the evenings.' ,'url':'https://th.bing.com/th/id/OIP.sAo-X-gba0_Q_-BpsTh22AHaE8?pid=ImgDet&rs=1'},
        {'place': 'Charminar','long':17.361570,'lat':78.474663 ,'temp':32 , 'type': 'Historical','details':'Charminar: A 16th-century monument located in the heart of Hyderabad, known for its four minarets and Islamic architecture. It is a popular landmark and a symbol of the citys history and culture.' ,'url':'https://upload.wikimedia.org/wikipedia/commons/7/71/Charminar_Hyderabad_1.jpg'},
        ],
    'Tripura': [
        {'place': 'Neermahal Palace','long':23.506639,'lat':91.315079 ,'temp':36 , 'type': 'Palace','details':'Neermahal Palace: A palace located in the middle of a lake in Melaghar, Tripura. It was built by the Tripura king as a summer retreat and has a unique blend of Hindu and Muslim architectural styles.','url':'https://i.ytimg.com/vi/JETec2Pe-HA/maxresdefault.jpg'},
        {'place': 'Unakoti Hill','long':24.313330,'lat':92.067253 ,'temp':36 , 'type': 'Historical','details':'Unakoti Hill: A hill located in Kailashahar, Tripura, known for its rock-cut sculptures and carvings. It has over 10,000 rock-cut images and is a popular destination for pilgrimage and sightseeing.','url':'https://www.worldatlas.com/r/w2000-h1125-q90/upload/32/18/52/img-4823.jpg'},
        {'place': 'Kamalasagar Kali Temple','long':23.740135,'lat':91.170715 ,'temp':34 , 'type': 'Religious','details':'Kamalasagar Kali Temple: A temple dedicated to the goddess Kali, located near the Bangladesh border in Tripura. It has a scenic location on the banks of a lake and is a popular destination for devotees.','url':'https://alchetron.com/cdn/kamalasagar-1669bfcc-2f1a-472b-9c06-fe97b8f8249-resize-750.jpg'},
        {'place': 'Jampui Hills','long':23.925320,'lat':92.273760 ,'temp':36 , 'type': 'Hill Station','details':'Jampui Hills: A hill station located in North Tripura district, known for its scenic beauty and panoramic views of the surrounding valleys. It is popular for trekking and outdoor activities.','url':'https://th.bing.com/th/id/OIP.YSvSFd4bvq9cJd5QiDWLMgHaE8?pid=ImgDet&rs=1'},
        {'place': 'Sepahijala Wildlife Sanctuary','long':23.668400,'lat':91.322823 ,'temp':37 , 'type': 'Wildlife','details':'Sepahijala Wildlife Sanctuary: A wildlife sanctuary located near Agartala, Tripura, known for its varied flora and fauna, including primates, birds, and orchids. It has a zoo, botanical garden, and lake for boating.' ,'url':'https://www.gosahin.com/go/p/c/1519496782_Sipahijala-Wildlife-Sanctuary4.jpg'},
        ],
        
    'Uttar Pradesh': [
        {'place': 'Taj Mahal','long':27.174820,'lat':78.042221 ,'temp':31 , 'type': 'Historical','details':'Taj Mahal: A UNESCO World Heritage site, Taj Mahal is an iconic ivory-white marble mausoleum located in Agra, Uttar Pradesh. It was commissioned by Mughal Emperor Shah Jahan in memory of his wife Mumtaz Mahal and is considered one of the most beautiful buildings in the world.' ,'url':'https://i0.wp.com/thepointsguy.com/wp-content/uploads/2019/06/GettyImages-936994634.jpg?fit=2097%2C1430px&ssl=1'},
        {'place': 'Varanasi Ghats','long':25.387722,'lat':82.972692 ,'temp':36 , 'type': 'Religious','details':'Varanasi Ghats: Varanasi, also known as Kashi or Banaras, is a city in Uttar Pradesh that is considered one of the holiest places in India. The ghats, or steps leading down to the river, are an important part of the citys religious and cultural heritage. People come to take a dip in the Ganges River to purify their souls and perform religious rituals.' ,'url':'https://www.solitarytraveller.com/wp-content/uploads/2020/09/varanasi_assi_ghat-min.jpg'},
        {'place': 'Fatehpur Sikri','long':27.094730,'lat':77.669680 ,'temp':30 , 'type': 'Historical','details':'Fatehpur Sikri: A fortified city located in the Agra district of Uttar Pradesh, Fatehpur Sikri was built by Mughal Emperor Akbar in the 16th century. It served as his capital for a short period before being abandoned due to water scarcity. The site contains several palaces, mosques, and other buildings that are well-preserved and offer a glimpse into Mughal architecture and culture.' ,'url':'https://static.toiimg.com/photo/msid-65839113,width-96,height-65.cms'},
        {'place': 'Allahabad Fort','long':25.429291,'lat':81.876953 ,'temp':30 , 'type': 'Historical','details':'Allahabad Fort: Located in Allahabad, Uttar Pradesh, this fort was built by Mughal Emperor Akbar in the late 16th century. It served as a military stronghold and administrative center for the Mughal Empire. The fort is now a popular tourist attraction and offers a panoramic view of the city.' ,'url':'https://4.bp.blogspot.com/-qZww2v0TKvI/Wg1dQd1MHyI/AAAAAAAAC64/S7xR1BIcCMwEEVscK_fdzPg7iN9s7FQ8QCLcBGAs/s1600/Allahabad%252C_Akbar_Fort%252C_from_river_2015-11-12.jpg'},
        {'place': 'Chandra Shekhar Azad Park','long':25.453550,'lat':81.847717 ,'temp':28 , 'type': 'Park','details':'Chandrashekhar Azad Park (also known by its former name Alfred Park, and Company Bagh during the Company Raj) is a public park in Prayagraj, Uttar Pradesh, India. Built in 1870 to mark Prince Alfreds visit to the city, with an area of 133 acres, it is the biggest park in Prayagraj.' ,'url':'https://www.tourmyindia.com/socialimg/chandra-shekhar-azad-park-prayagraj.jpg'},
        ],
    'Uttarakhand': [
        {'place': 'Valley of Flowers National Park','long':30.553730, 'lat':79.563606 ,'temp':18 , 'type': 'National Park','details':'Valley of Flowers National Park: It is a national park located in the Chamoli district of Uttarakhand. It is known for its vibrant alpine flowers that bloom in a valley surrounded by snow-capped mountains. The park is open to visitors from June to October.' ,'url':'https://backiee.com/static/wpdb/wallpapers/1000x563/188852.jpg'},
        {'place': 'Kedarnath Temple','long':30.735241,'lat':79.066887 ,'temp':34 , 'type': 'Religious','details':'Kedarnath Temple: It is a Hindu temple dedicated to Lord Shiva located in the Rudraprayag district of Uttarakhand. It is one of the four Char Dham pilgrimage sites and is considered to be one of the holiest shrines in Hinduism.' ,'url':'https://www.bizarexpedition.com/images/kedar.jpg'},
        {'place': 'Rishikesh','long':30.107700,'lat':78.287800 , 'temp':29 ,'type': 'Spiritual','details':'Rishikesh: It is a city located in the foothills of the Himalayas in Uttarakhand. It is known as the "Yoga Capital of the World" and is a popular destination for spiritual seekers, yoga enthusiasts, and adventure sports enthusiasts. It is also home to several ancient temples and ashrams.' ,'url':'https://lp-cms-production.imgix.net/2019-06/GettyImages-181606492_medium.jpg?fit=crop&q=40&sharp=10&vib=20&auto=format&ixlib=react-8.6.4'},
        {'place': 'Nainital','long':29.398050,'lat':79.444540 , 'temp':13 ,'type': 'Hill Station','details':'Nainital: It is a picturesque hill station located in the Kumaon region of Uttarakhand. It is known for its beautiful Naini Lake, surrounded by lush green hills. The town is also famous for its scenic views, trekking opportunities, and ancient temples.' ,'url':'https://www.visittnt.com/blog/wp-content/uploads/2018/12/Nainital-1.jpg'},
        {'place': 'Jim Corbett National Park','long':29.383070,'lat':79.117920 ,'temp':28 , 'type': 'Wildlife','details':'Jim Corbett National Park: It is a wildlife sanctuary located in the Nainital district of Uttarakhand. It is known for its diverse flora and fauna, including the Bengal tiger, Indian elephant, and several species of deer and birds. The park offers several opportunities for jungle safaris and wildlife spotting.' ,'url':'https://ilovetripping.com/wp/wp-content/uploads/2015/04/JC3.jpg'},
        ],
    'West Bengal': [
        {'place': 'Victoria Memorial','long':22.545868,'lat':88.347908 ,'temp':26 , 'type': 'Historical','details':'Victoria Memorial: It is a historical monument built during the British Raj in Kolkata. It is now a museum that showcases various artifacts and exhibits from the colonial era.'  ,'url':'https://thirdeyetraveller.com/wp-content/uploads/VICTORIAMEMORIAL-17-of-25-1440x1080.jpg'},
        {'place': 'Sundarbans','long':21.868349,'lat':88.889503 ,'temp':32 , 'type': 'National Park','details':'Sundarbans: It is a UNESCO World Heritage site and a national park located in the delta region of the Ganges, Brahmaputra, and Meghna rivers. It is famous for its unique mangrove forests and is home to the Royal Bengal tiger.' ,'url':'https://cdn.thewire.in/wp-content/uploads/2020/05/07130306/Sundarban_Tiger.jpg'},
        {'place': 'Darjeeling','long':27.040630,'lat':88.258620 , 'temp':17 ,'type': 'Hill Station','details':'Darjeeling: It is a picturesque hill station located in the foothills of the Himalayas. It is famous for its tea plantations, scenic beauty, and the Darjeeling Himalayan Railway, a UNESCO World Heritage site.' ,'url':'https://imgcld.yatra.com/ytimages/image/upload/v1462443339/Darjeeling_Map2.jpg'},
        {'place': 'Howrah Bridge','long':22.585100,'lat': 88.346901 , 'temp':26 ,'type': 'Historical','details':' It is an iconic suspension bridge that spans the Hooghly River in Kolkata. It was built in 1943 and is one of the busiest bridges in the world.' ,'url':'https://procaffenation.com/wp-content/uploads/2017/04/beautiful-view-of-howrah-bridge-at-evening-compressor.jpg'},
        {'place': 'Bishnupur','long':23.075000,'lat': 87.317000 , 'temp':24 ,'type': 'Historical','details':'Bishnupur: It is a small town in the Bankura district of West Bengal. It is known for its terracotta temples built during the 17th and 18th centuries by the Malla kings.' ,'url':'https://static.toiimg.com/photo/68741292/bishnupur-temples.jpg?width=748&resize=4'},
        ],
    }

from django.shortcuts import render



import folium
import random


from folium.plugins import PolyLineTextPath
def state_detail(request):
    if request.method == 'POST':
        state_name = request.POST.get('state_name')
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')
        num_people = request.POST.get('num_people')
        companions = request.POST.get('companions')
        current_l = [30.3165, 78.0322]

        # Convert date strings to datetime objects
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

        # Calculate number of days between start date and end date
        num_days = (end_date - start_date).days

        if state_name in datavalue:
            state_data = datavalue[state_name]

            # Filter places based on number of days
            if num_days:
                state_data = [place for place in state_data if 'type' in place and place['type'] != 'None']
                random.shuffle(state_data)  # Shuffle the list randomly
                state_data = state_data[:int(num_days)]

            # Create a list of tuples with the longitude and latitude values for each place
            coordinates = [(place['long'], place['lat']) for place in state_data]

            # Create a folium map object
            my_map = folium.Map(location=[20.5937, 78.9629], zoom_start=10)

            # Add markers to the map for each coordinate
            for place in state_data:
                coordinate = (place['long'], place['lat'])
                place_name = place['place']
                folium.Marker(location=coordinate, popup=place_name).add_to(my_map)

             #Add current location marker
            folium.Marker(location=current_l, popup='Current Location').add_to(my_map)

            # Connect current location with lines
            for coordinate in coordinates:
                folium.PolyLine(locations=[current_l, coordinate], weight=1, color='red').add_to(my_map)


            # Create a list of lines between the coordinates
            lines = folium.PolyLine(locations=coordinates, weight=2, color='blue')

            # Add the lines to the map
            lines.add_to(my_map)

            # Convert the map object to HTML
            map_html = my_map._repr_html_()

            con = "Dehradun"
#            # Pass the map HTML to the context dictionary and render the template
            context = {'state_data': state_data, 'state_name': state_name, 'num_days': num_days,
                       'start_date_str': start_date_str, 'end_date_str': end_date_str, 'map_html': map_html,
                       'con':con,'current_l':current_l}
            return render(request, 'home2/state_details.html', context)


        else:
            error_msg = 'Sorry, we do not have any information for the state you entered.'
            context = {'error_msg': error_msg}
            return render(request, 'home2/state_details.html', context)
    else:
        return render(request, 'home2/state_details.html')
    

#############################state_val_end####################################


# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# import pickle

# # Load the saved components
# with open('count_vectorizer.pkl', 'rb') as f:
#     cv = pickle.load(f)

# with open('similarity_matrix.pkl', 'rb') as f:
#     similarity_matrix = pickle.load(f)

# with open('index_destination_dict.pkl', 'rb') as f:
#     index_destination_dict = pickle.load(f)

# with open('destination_index_dict.pkl', 'rb') as f:
#     destination_index_dict = pickle.load(f)

# @csrf_exempt
# def recommend_place(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             destination = data['destination']
#             number_of_recommendations = int(data['number_of_recommendations'])
            
#             if destination not in destination_index_dict:
#                 return JsonResponse({'error': 'Destination not found'}, status=404)

#             idx = destination_index_dict[destination]
#             similarity_list = similarity_matrix[idx]
            
#             lst = [(similarity_list[i], i) for i in range(len(similarity_list))]
#             lst.sort(reverse=True)
            
#             recommendations = [index_destination_dict[lst[i][1]] for i in range(len(lst))]
#             recommendations.remove(destination)
            
#             context = {
#                 'destination': destination,
#                 'number_of_recommendations': number_of_recommendations,
#                 'recommendations': recommendations[:number_of_recommendations]
#             }
            
#             return JsonResponse(context)
        
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)
    
#     else:
#         return render(request, 'home2/recommend_place.html')


##  Code for Recommend with image ##########


from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pickle
import requests

# Load the saved components
with open('count_vectorizer.pkl', 'rb') as f:
    cv = pickle.load(f)

with open('similarity_matrix.pkl', 'rb') as f:
    similarity_matrix = pickle.load(f)

with open('index_destination_dict.pkl', 'rb') as f:
    index_destination_dict = pickle.load(f)

with open('destination_index_dict.pkl', 'rb') as f:
    destination_index_dict = pickle.load(f)

UNSPLASH_ACCESS_KEY = '79IxkUQT9iNylw9fOxrGqlUa2Aj5UoVf0-NrdpJtQTc'  # Replace with your Unsplash API key

def get_unsplash_image(query):
    url = f"https://api.unsplash.com/search/photos?query={query}&client_id={UNSPLASH_ACCESS_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return data['results'][0]['urls']['small']
    return ''

@csrf_exempt
def recommend_place(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            destination = data['destination']
            number_of_recommendations = int(data['number_of_recommendations'])
            
            if destination not in destination_index_dict:
                return JsonResponse({'error': 'Destination not found'}, status=404)

            idx = destination_index_dict[destination]
            similarity_list = similarity_matrix[idx]
            
            lst = [(similarity_list[i], i) for i in range(len(similarity_list))]
            lst.sort(reverse=True)
            
            recommendations = [index_destination_dict[lst[i][1]] for i in range(len(lst))]
            recommendations.remove(destination)

            results = []
            for rec in recommendations[:number_of_recommendations]:
                image_url = get_unsplash_image(rec)
                results.append({'place': rec, 'image_url': image_url})
            
            context = {
                'destination': destination,
                'number_of_recommendations': number_of_recommendations,
                'recommendations': results
            }
            
            return JsonResponse(context)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    else:
        return render(request, 'home2/recommend_place.html')


######Recommend Functions on the basis of city name End #######












import pickle
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

# Load your processed data
df = pd.read_csv('travel_destinations.csv')

# Drop unnecessary columns
columns_to_drop = ['Tags', 'State', 'Old_age', 'Young_age', 'link 1',
       'Avg Expense Per Day', 'historical & heritage', 'city', 'pilgrimage',
       'hill station', 'beach', 'lake & backwater', 'adventure / trekking',
       'wildlife', 'waterfall', 'nature & scenic', 'keys']
df.drop(columns_to_drop, axis=1, inplace=True)

# Create a dictionary mapping index to city name
index_destination_dict = {i: df.loc[i, 'City'] for i in range(len(df))}

# Load new_corpus
with open('new_corpus_2.pkl', 'rb') as f:
    new_corpus = pickle.load(f)

# Load CountVectorizer object
with open('count_vectorizer_2.pkl', 'rb') as f:
    cv = pickle.load(f)

# Load correlation matrix
with open('correlation_matrix_2.pkl', 'rb') as f:
    new_correlationMatrix = pickle.load(f)

# Function to preprocess user input
def preprocess_query(query):
    wl = WordNetLemmatizer()

    # Remove Hyperlinks
    processed_query = re.sub(r"http\S+", ' ', query)
    
    # Remove Punctuation Marks and Special Symbols
    processed_query = re.sub('[^a-zA-Z0-9]', ' ', processed_query)
    
    # Lowercase
    processed_query = processed_query.lower()
    
    # Tokenization
    processed_query = processed_query.split()
    
    # Remove Stopwords and perform Lemmatization
    processed_query = [wl.lemmatize(word, pos='v') for word in processed_query if not word in stopwords.words('english')]
    processed_query = ' '.join(processed_query)
    
    return processed_query

# Function to recommend destinations based on user input
def recommend_destinations(query):
    # Pre-process query
    processed_query = preprocess_query(query)
    
    # Update new_corpus with processed_query
    new_corpus.append(processed_query)
    
    # Transform new_corpus with CountVectorizer
    new_X = cv.transform(new_corpus)
    new_vectors = new_X.toarray()
    
    # Compute similarity with the updated corpus
    new_correlationMatrix = cosine_similarity(new_vectors)
    
    # Get recommendations
    list_of_tuples = []
    for i in range(len(df)):
        list_of_tuples.append((new_correlationMatrix[-1][i], i))
    sorted_list_of_tuples = sorted(list_of_tuples, reverse=True)
    
    # Return top 10 recommendations
    top_recommendations = []
    for element in sorted_list_of_tuples[:10]:
        top_recommendations.append(index_destination_dict[element[1]])
    
    return top_recommendations

# Define a view for the home page
def recommend_place_mood(request):
    return render(request, 'home2/recommend_place_mood.html')

# Define a view for the recommendation results
def recommend_mood_result(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        recommendations = recommend_destinations(query)
        return render(request, 'home2/recommend_mood_result.html', {'query': query, 'recommendations': recommendations})
    else:
        return HttpResponse("Method not allowed", status=405)









import folium
import random
from datetime import datetime


from django.shortcuts import render
from django.http import HttpResponse


def add_place(request):
    if request.method == 'POST':
        state_name = request.POST.get('state_name')
        place = request.POST.get('place')
        longitude = float(request.POST.get('longitude'))
        latitude = float(request.POST.get('latitude'))
        temp = int(request.POST.get('temp'))
        place_type = request.POST.get('type')
        details = request.POST.get('details')
        url = request.POST.get('url')

        new_place = {
            'place': place,
            'long': longitude,
            'lat': latitude,
            'temp': temp,
            'type': place_type,
            'details': details,
            'url': url,
        }

        if state_name in datavalue:
            datavalue[state_name].append(new_place)
        else:
            datavalue[state_name] = [new_place]

        return redirect('state_detail')
    else:
        return render(request, 'home2/add_place.html')


from django.shortcuts import render
from .models import UserReview

def save_review(request):
    if request.method == 'POST':
        state_name = request.POST['state_name']
        
        rating = request.POST['rating']
        
        user_review = UserReview(state_name = state_name , rating=rating)
        user_review.save()
        
        # Optionally, you can redirect to a success page
        return HttpResponse("Thankyou for the review!!!  <a href='http://127.0.0.1:8000/'>HOME</a>")
    else:
        return render(request, 'home2/review_form.html')
