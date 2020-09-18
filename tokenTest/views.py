import hashlib
import time

from django.shortcuts import render

# Create your views here.
from sessionTest.models import SessionTest


def home(request):
    return render(request,'home.html')


def login(request):
    if request.method == 'GET':
        return render(request,'tokenTest/login.html')
    if request.method == 'POST':
        request.session.flush()
        username = request.POST.get('username')
        password = request.POST.get('password')
        token = tokenGenerator(request.META['REMOTE_ADDR'],username)
        student = SessionTest(
            s_name = username,
            s_password = password,
            s_token =token
        )
        request.session['username'] = username
        request.session['password'] = password
        request.session['token'] = str(token)
        student.save()
        context = {
            'username': username,
            'password':password,
                   }
        return render(request,'tokenTest/center.html',context)

def tokenGenerator(ip ,username):
    token = hashlib.new('md5',(ip + username + time.ctime()).encode('utf-8')).digest()
    print(token)
    return token