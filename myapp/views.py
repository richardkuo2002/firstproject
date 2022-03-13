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

def listone(request, searchname): 
    try: 
        unit = student.objects.get(sName=searchname) #讀取一筆資料
    except:
        errormessage = " (讀取錯誤!)"
    return render(request, "listone.html", locals())

def listall(request):  
    students = student.objects.all().order_by('id')  
    #讀取資料表, 依 id 遞增排序(欄位前加入負號-id代表遞減排序)
    return render(request, "listall.html", locals())

def insert(request):  #新增資料
    sName = '林三和'
    sSex =  'M'
    sBirthday =  '1987-12-26'
    sEmail = 'bear@superstar.com'
    sPhone =  '0963245612'
    sAddr =  '台北市信義路18號'
    unit = student.objects.create(sName=sName, sSex=sSex, sBirthday=sBirthday, sEmail=sEmail, sPhone=sPhone, sAddr=sAddr) 
    unit.save()  #寫入資料庫
    students = student.objects.all().order_by('-id')  #讀取資料表, 依 id 遞減排序
    return render(request, "listall.html", locals())

def modify(request):  #修改資料
    unit = student.objects.get(sName='林三和')
    unit.sBirthday =  '1987-12-11'
    unit.sAddr = '台北市信義路234號'
    unit.save()  #寫入資料庫
    students = student.objects.all().order_by('-id')
    return render(request, "listall.html", locals())

def delete(request, deletname, id=None):  #刪除資料
    unit = student.objects.get(sName=deletname)
    unit.delete()
    students = student.objects.all().order_by('-id')
    return render(request, "listall.html", locals())