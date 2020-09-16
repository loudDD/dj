from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def set_cookie(request):
    response = HttpResponse("设置cookie")
    # response.set_cookie('username', 'tom')
    return response


def get_cookie(request):
    a = request.COOKIES.get('username')
    print(a )
    return HttpResponse(a)


def login(request):


    return render(request,'login.html')


def success(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        print(username)
        response = render(request,'login.html')
        response.set_cookie('name',username)获取为None
        print(request.COOKIES.get('name'))
    username = request.COOKIES.get("name")
    # response = redirect(reverse('login:success'))
    return HttpResponse(username)