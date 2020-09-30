import os

from django.core.cache import cache
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page

from Two.models import TwoIdcardIdPerson, TwoIdcard, TwoCat, TwoDog, testupload


def add_person(request):
    username = request.GET.get('username')
    person = TwoIdcardIdPerson()
    person.p_name = username
    person.save()
    return HttpResponse('person 添加成功 %d' % person.id)


def add_idcard(request):
    id_num = request.GET.get('id_num')
    idcard = TwoIdcard()
    idcard.id_num = id_num
    idcard.save()
    return HttpResponse('id card 添加成功%s' % idcard.id_num)


# def bind_card(request): # 1:1
#     person = Person.objects.last()
#     idcard= IDCard.objects.last()
#     idcard.id_person = person
#     idcard.save()
#     return HttpResponse('绑定成功')

# def bind_card(request): #1:n
#     person = Person.objects.last()
#     idcard = IDCard.objects.last()
#     idcard.id_person = person
#     idcard.save()
#     idcard = IDCard.objects.first()
#     idcard.id_person = person
#     idcard.save()
#     return HttpResponse('绑定成功')
def bind_card(request):  # m:n
    person = TwoIdcardIdPerson.objects.first()
    idcard = TwoIdcard.objects.last()
    # idcard.id_person.add(person)
    person.idcard_set.add(idcard)
    idcard.save()

    return HttpResponse('绑定成功')


def up(request):
    if request.method == 'POST':
        file = request.FILES.get('')
        with open("", 'wb') as f:
            for i in file.chunks():
                f.write(i)
                f.flush()


def removeperson(request):
    person = TwoIdcardIdPerson.objects.last()
    person.delete()
    return HttpResponse('移除 person成功')


def removecard(request):
    idcard = TwoIdcard.objects.last()
    idcard.delete()
    return HttpResponse('删除id 成功')


def getcard(request):
    person_id = request.GET.get('id')
    card = TwoIdcard.objects.get(twoidcardidperson=person_id).id_num
    return HttpResponse("the card id {}".format(card))


def getperson(request):
    id_num = request.GET.get('id')
    person = TwoIdcardIdPerson.objects.get(pk=id_num).p_name
    return HttpResponse('the person is {}'.format(person))


def getallcard(request):
    # person = Person.objects.last()  从获取主
    # idcards = person.idcard_set.all()

    idcards = TwoIdcard.objects.last()  # 主获取从
    persons = idcards.id_person.all()
    print(type(persons))
    for i in persons:
        print(i)
    return render(request, 'show.html', context={'showlist': persons})


def addcat(request):
    Cat = TwoCat()
    Cat.a_name = "catty1"
    Cat.d_eat = "ok"
    Cat.save()
    return HttpResponse("cat create success {} ".format(Cat.id))


def adddog(request):
    Dog = TwoDog()
    Dog.d_leg = "4"
    Dog.d_eat = "no"
    Dog.save()
    return HttpResponse("dog create success {}".format(Dog.id))


def upload(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    elif request.method == 'POST':
        img = testupload()
        img.t_name = request.POST.get('username')
        print(request.FILES.get('icon'))
        img.t_img = request.FILES.get('icon')
        img.save()
        # return HttpResponse('上传成功')
        img = testupload.objects.first()
        username = img.t_name
        image = img.t_img.url
        print("path", image)
        print(type(img.t_img.url))
        print(username)
        print("url", img.t_img.url)
        data = {
            'username': username,
            # 'image': image,
            'image': image,
        }
        return render(request, 'Two/center.html', context=data)


@cache_page(timeout=30, cache='redis_cache')
def getupload(request):
    page = int(request.GET.get('page', 1))
    per_page = int(request.GET.get('per_page', 10))

    uploaded_list = testupload.objects.all()[per_page * (page - 1): per_page * page]
    context = {'uploaded_list': uploaded_list}
    return render(request, 'two/uploaded.html', context=context)


def manualcache(request):
    result = cache.get('cacheunqiuelocaotr')
    if result:
        return HttpResponse(result)
    uploaded_list = testupload.objects.all()
    context = {'uploaded_list': uploaded_list}
    response = render(request, 'two/uploaded.html', context=context)
    cache.set('cacheunqiuelocaotr', response.content, timeout=30)
    return response


def hello(request):
    return HttpResponse('hello')


def error(request):
    return HttpResponse(19 / 0)


def uploadswithpage(request,pageurl):
    # page = int(request.GET.get('page', 1))
    # per_page = int(request.GET.get('per_page', 10))
    per_page = 10

    uploaded_list = testupload.objects.all()

    paginator = Paginator(uploaded_list, per_page=per_page)
    pageobject = paginator.page(pageurl)

    context = {
        'pageobject': pageobject
    }
    return render(request, 'Two/uploadedwithpage.html', context=context)
