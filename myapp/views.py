from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def sayhello(request):
    return HttpResponse("Hello Django")

def sayhello2(request,showname):
    return HttpResponse("Hello"+showname)
def sayhello3(request,showname):
    now=datetime.now()
    return render(request,"sayhello3.html",locals())
