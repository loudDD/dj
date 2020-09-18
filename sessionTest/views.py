from random import random

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def index(request):
    note = "This is the index page of sessionTest"
    name = None
    
    try:
        name = request.session.get("username")
    except :
        pass
    if request.method == 'POST':
        print(request.POST.get('username'))
        request.session['username'] = request.POST.get('username')
        print(request.session.get('username'))
        return redirect(reverse('session:index'))
    return render(request,'sessionTest/index.html',context={'pagename': "index", 'note': note , 'name': name})


def login(request):
    if request.method == "GET":
        return render(request,'sessionTest/login.html')
