from django.contrib import admin
from . models import orders,status

# Register your models here.

class Adminorders(admin.ModelAdmin):
    list_display = ['product','customer','quantity','price','date','landmark','city','pincode','phone','orderStatus']

class Adminstatus(admin.ModelAdmin):
    list_display = ['status','id']









admin.site.register(orders,Adminorders)
admin.site.register(status,Adminstatus)


