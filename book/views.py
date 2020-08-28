from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo
# Create your views here.

def indexpage(request):
    books = BookInfo.objects.all()
    week = ["Monday","Tuesday","Wednesday","Thusday","Friday","Saturday","Sunday"]
    context = {"name": "tom",
               "books":books,
               "week":week
               }

    return render(request, "index.html", context)
    # return HttpResponse('index')


def getdata(request):
    return render(request, 'data.html', {"time": "today"})
