"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
#from django.conf.urls import url
from myapp import views
from myapp.views import sayhello, sayhello2, sayhello3, listone, listall

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',sayhello),
    url(r'^sayhello2/(\w+)$',sayhello2),
    url(r'^sayhello3/(\w+)$',sayhello3),
    url(r'^listone/(\w+)$',listone),
    # url(r'^listone/$',listone),
    url(r'^listall/$', listall),
    url(r'^insert/$', views.insert),   #新增資料
    url(r'^modify/$', views.modify),   #修改資料
    url(r'^delete/$', views.delete),   #刪除資料
]
