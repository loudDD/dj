from django.shortcuts import render

# Create your views here.
from students.models import Class_List, Students


def classes(request):
    classlist = Class_List.objects.all()
    context = {"classlist" : classlist}
    return render(request,'classes.html',context)


def insert(request):
    # Class_List.objects.create(c_name="classone")
    # Class_List.objects.create(c_name="classtwo")
    # Class_List.objects.create(c_name="class3")
    class1 = Class_List.objects.get(pk=1)
    class2 = Class_List.objects.get(pk=2)
    Students.objects.create(s_name="tom1",s_class=class1)
    Students.objects.create(s_name="jerry2",s_class=class1)
    Students.objects.create(s_name="lily3",s_class=class2)

    return render(request,'insert_data.html')


def students(request,class_id):
    students_list = Students.objects.filter(s_class=class_id)
    context = {"students_list":students_list}
    return render(request,'students_list.html',context)


def gender(request):
    #增加学生性别
    #可以删除学生，添加学生
    return