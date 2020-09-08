from django.shortcuts import render
from register.models import RegisterInfo


# Create your views here.
def register(request):
    RegisterInfo.objects.create(
        name="tom",
        password="123"
    )
    context = {
        'register_data': RegisterInfo.objects.all(),
    }
    print(111)
    print(context)
    if request.method == 'POST':
        info = RegisterInfo(
            name=request.POST['username'],
            password=request.POST['password']
        )
        info.save()

    return render(request, 'register.html', context)
