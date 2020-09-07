from django.urls import path
from book import views as bookview

urlpatterns = [
    path('add/', bookview.addData),
    path('delete/', bookview.deleteData),
    path('update/', bookview.updateData),
    path('get/', bookview.getData),
    path('book/', bookview.getdata, name='book'),
    path('getsum/', bookview.getsum)
]
