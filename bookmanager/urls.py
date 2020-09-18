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
from book import views as bookview
from pay import views as payview
from vote import views as voteview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('res/', bookview.response),
    path('index/', bookview.indexpage),
    path('data/', bookview.getdata),
    path('time/', payview.getweek),
    # path('register/', registerview.register),
    path('book/', include('book.urls')),
    path("", bookview.firstpage, name='home'),
    path(r"home/", bookview.gethome),
    path(r"home_one/", bookview.gethome_one),
    path('vote/', include("vote.urls")),
    path('students/', include('students.urls')),
    path('cookie/', include('cookie.urls')),
    path('session/',include('sessionTest.urls')),

]
