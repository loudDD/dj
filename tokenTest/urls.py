from django.urls import path

from tokenTest import views

app_name = 'token'
urlpatterns = [
    path("",views.home,name="home"),
    path("login",views.login,name="login"),
    # path("center",views.center,name="center"),

]