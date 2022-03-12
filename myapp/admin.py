from django.contrib import admin
from myapp.models import student
# Register your models here.

class studentadmin(admin.ModelAdmin):
    #使用list_display顯示多個欄位
    list_display=('id','sName','sSex','sBirthday','sEmail','sPhone','sAddress')
    #使用list_filter資料過濾
    list_filter=('sName','sPhone')
    #使用search_fields依照欄位搜尋
    search_fields=('sName',)
    #使用ordering排序
    ordering=('id',)
    #ordering=('-id',) 

admin.site.register(student, studentadmin)