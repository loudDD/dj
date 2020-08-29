from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo
from django.db.models import Q, F, Sum


# Create your views here.

def indexpage(request):
    '''
    #F对象，求 readcount 小于id
    readcountlessOne = BookInfo.objects.filter(readcount__lt=F('id'))
    #Q对象
    les = BookInfo.objects.filter(Q(id__gt=1) & Q(readcount__gt=50))
    # 聚合函数
    sum = BookInfo.objects.aggregate(Sum('readcount'))
    #排序 默认升序
    BookInfo.objects.all().order_by('readcount')
    BookInfo.objects.all().order_by('-readcount')
    '''
    # print(datetime.now())
    # book = BookInfo.objects.all()
    # book.delete()
    # BookInfo.objects.create(
    #     name="西游记",
    #     pub_date=datetime.strptime("2020-01-01" , "%Y-%m-%d"),
    #     commentcount=20,
    #     readcount=32
    # )
    # BookInfo.objects.create(
    #     name="红楼梦",
    #     pub_date=datetime.strptime("2010-01-01" , "%Y-%m-%d"),
    #     commentcount=24,
    #     readcount=50
    # )
    # BookInfo.objects.create(
    #     name="水浒传",
    #     pub_date=datetime.strptime("2001-01-01" , "%Y-%m-%d"),
    #     commentcount=2,
    #     readcount=200
    # )
    # book = BookInfo(
    #     name='三国演义',
    #     pub_date=datetime.now(),
    #     commentcount=43,
    #     readcount=100
    # )
    # book.save()
    books = BookInfo.objects.all()
    times = books.filter(pub_date__isnull=False).values("pub_date")
    time = [x['pub_date'].strftime('%Y-%m-%d ') for x in times]
    week = ["Monday", "Tuesday", "Wednesday", "Thusday", "Friday", "Saturday", "Sunday"]
    context = {"name": "tom",
               "books": books,
               "week": week,
               'pub_date': time,
               }

    return render(request, "index.html", context)
    # return HttpResponse('index')


def getdata(request):
    return render(request, 'data.html', {"time": "today"})
