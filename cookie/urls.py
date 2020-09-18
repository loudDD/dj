from django.urls import path

from cookie import views

app_name = 'cookie'
urlpatterns = [
    path('setcookie/', views.set_cookie, name='set_cookie'),
    path('getcookie/', views.get_cookie, name='get_cookie'),
    path('login/', views.login, name='login'),
    path('success/', views.success, name='success'),
    path('logout/',views.logout, name='logout')
]
