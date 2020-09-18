from django.urls import path

from sessionTest import views

app_name = 'session'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
]
