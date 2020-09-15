from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from students.models import Class_List, Students


def classes(request):
    classlist = Class_List.objects.all()
    context = {"classlist": classlist}
    return render(request, 'classes.html', context)


def insert(request):
    # Class_List.objects.create(c_name="classone")
    # Class_List.objects.create(c_name="classtwo")
    # Class_List.objects.create(c_name="class3")
    class1 = Class_List.objects.get(pk=1)
    class2 = Class_List.objects.get(pk=2)
    Students.objects.create(s_name="tom1", s_class=class1)
    Students.objects.create(s_name="jerry2", s_class=class1)
    Students.objects.create(s_name="lily3", s_class=class2)

    return render(request, 'insert_data.html')


def students(request, class_id):
    students_list = Students.objects.filter(s_class=class_id)
    context = {"students_list": students_list}
    return render(request, 'students_list.html', context)


def gender(request):
    # 可以删除学生，添加学生
    return


def add(request):
    if request.method == "GET":
        return render(request, 'add.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        _class = request.POST.get('class')
        gender = request.POST.get('gender')
        realclass = Class_List.objects.get(pk=_class)
        Students.objects.create(
            s_name=name,
            s_class=realclass,
            s_gender=gender
        )
        if Students.objects.filter(s_name=name):
            return HttpResponse("添加成功")
        else:
            return HttpResponse('添加失败')



def delete(request):
    if request.method == "GET":
        return render(request, 'delete.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        Students.objects.get(s_name=name).delete()
        if not Students.objects.filter(s_name=name):
            return HttpResponse("删除成功")
        else:
            return HttpResponse('删除失败')

def test(request):
    print(request.path)
    print(request.method)
    print(request.GET)
    print(request.POST)
    return HttpResponse("ok")