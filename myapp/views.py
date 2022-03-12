from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from googlesearch import search
from myapp.models import student

# Create your views here.

def sayhello(request):
    return HttpResponse("Hello Django")

def sayhello2(request,showname):
    return HttpResponse("Hello"+showname)

def sayhello3(request,showname):
    now=datetime.now()
    return render(request,"sayhello3.html",locals())

def listone(request): 
    try: 
        unit = student.objects.get(cName="郭睿桓") #讀取一筆資料
    except:
        errormessage = " (讀取錯誤!)"
    return render(request, "listone.html", locals())