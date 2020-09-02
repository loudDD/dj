"""bookmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import book
import pay
import register
from book import views as bookview
from pay import views as payview
from register import urls,views as registerview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', bookview.indexpage),
    path('data/', bookview.getdata),
    path('time/', payview.getweek),
    # path('register/', registerview.register),
    path('re/', include('register.urls')),
    path('book/', include('book.urls')),

]
