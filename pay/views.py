import time

from django.shortcuts import render


# Create your views here.

def getweek(request):
    context = {"time": time.strftime("%Y-%m-%d ")}
    return render(request, 'data.html', context)
