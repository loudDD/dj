from datetime import datetime

from django.shortcuts import render
from book.models import BookInfo, CustomerInfo


# Create your views here.

def updateData(request):
    book = BookInfo.objects.get(pk=2)
    book.name = 'David'
    context = {
        'books': BookInfo.objects.all()
    }

    return render(request, 'index.html', context)


def addData(request):
    BookInfo.objects.create(
        name="西游记",
        pub_date=datetime.strptime("2020-01-01", "%Y-%m-%d"),
        commentcount=20,
        readcount=32
    )
    BookInfo.objects.create(
        name="红楼梦",
        pub_date=datetime.strptime("2010-01-01", "%Y-%m-%d"),
        commentcount=24,
        readcount=50
    )
    BookInfo.objects.create(
        name="水浒传",
        pub_date=datetime.strptime("2001-01-01", "%Y-%m-%d"),
        commentcount=2,
        readcount=200
    )
    book = BookInfo(
        name='三国演义',
        pub_date=datetime.now(),
        commentcount=43,
        readcount=100
    )
    book.save()
    context = {
        'books': BookInfo.objects.all()
    }
    return render(request, 'index.html', context)


def deleteData(request):
    data = BookInfo.objects.get(pk=2)
    data.delete()
    data.save()
    context = {
        'books': BookInfo.objects.all()
    }
    return render(request, 'index.html', context)


def getData(request):
    context = {
        'books': BookInfo.objects.all()
    }

    return render(request, 'index.html', context)


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

    book = BookInfo()

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


def getsum(request):
    customer = CustomerInfo.objects.all()
    context = dict(customer=customer)
    return render(request, "customer_info.html", context)


def firstpage(request):
    return render(request, 'firstpage.html')


def gethome(request):
    return render(request, "home.html", context={"title": "homepage"})


def gethome_one(request):
    return render(request, "home_one.html", context={"title": "homepage"})


def students(request):
    return render(request,'students.html',context={"id" : "10"})

def student(request,id):
    return render(request,'students.html',context={"id" : id})