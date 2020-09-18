import base64
from datetime import timedelta, datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse


def set_cookie(request):
    response = HttpResponse("设置cookie")
    # response.set_cookie('username', 'tom')
    return response


def get_cookie(request):
    a = request.COOKIES.get('username')
    print(a)
    return HttpResponse(a)


def login(request):
    return render(request, 'login.html')


def success(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        print(username)
        print(request.COOKIES.get('name'))
        name = request.COOKIES.get("name")
        # if name is not None:
        #     name = base64.decodebytes(bytes(name, encoding='utf-8'))
        # name = request.GET.get("name")
        try:
            name = request.get_signed_cookie('name')
        except:
            pass
        context = {
            'name': name
        }
        response = render(request, 'success.html', context)
        # response.set_cookie('name', username,expires=timedelta(days=1))
        # response.set_cookie('name', username,expires=timedelta(days=1))
        response.set_cookie('name', username, max_age=10)
        response.set_signed_cookie('name', username,salt="abc")
        # response.set_cookie('name', base64.encodebytes(bytes(username, encoding='utf-8')), max_age=10)
        # 再次刷新后，获取最新的cookie
        return response

    # response = redirect(reverse('login:success'))
    return HttpResponse("ok")


def logout(request):
    res = redirect(reverse('cookie:login'))
    res.delete_cookie('name')
    return res