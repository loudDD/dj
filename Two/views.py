from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Two.models import Person, IDCard


def add_person(request):
    username = request.GET.get('username')
    person = Person()
    person.p_name = username
    person.save()
    return HttpResponse('person 添加成功 %d' % person.id)


def add_idcard(request):
    id_num = request.GET.get('id_num')
    idcard = IDCard()
    idcard.id_num = id_num
    idcard.save()
    return HttpResponse('id card 添加成功%s' %idcard.id_num)


# def bind_card(request): # 1:n
#     person = Person.objects.last()
#     idcard= IDCard.objects.last()
#     idcard.id_person = person
#     idcard.save()
#     return HttpResponse('绑定成功')

def bind_card(request):
    person = Person.objects.last()
    idcard= IDCard.objects.last()
    idcard.id_person = person
    idcard.save()
    idcard= IDCard.objects.first()
    idcard.id_person = person
    idcard.save()
    return HttpResponse('绑定成功')

def removeperson(request):
    person = Person.objects.last()
    person.delete()
    return HttpResponse('移除 person成功')


def removecard(request):
    idcard = IDCard.objects.last()
    idcard.delete()
    return HttpResponse('删除id 成功')


def getcard(request):
    person_id = request.GET.get('id')
    card = IDCard.objects.get(id_person=person_id).id_num
    return HttpResponse("the card id {}".format(card))


def getperson(request):
    id_num = request.GET.get('id')
    person = Person.objects.get(pk=id_num).p_name
    return HttpResponse('the person is {}'.format(person))