from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Two import views

urlpatterns = [
    path('addperson/', views.add_person, name='add_person'),
    path('addidcard/', views.add_idcard, name='add_idcard'),
    path('bindcard/', views.bind_card, name='bind_card'),
    path('removeperson/', views.removeperson, name='removeperson'),
    path('removecard/', views.removecard, name='removecard'),
    path('getcard/', views.getcard, name='getcard'),
    path('getperson/', views.getperson, name='getperson'),
    path('getallcard/', views.getallcard, name='getallcard'),
    path('addcat/', views.addcat, name='addcat'),
    path('adddog/', views.adddog, name='adddog'),
    path('upload/',views.upload,name='upload')
]

