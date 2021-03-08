from django.contrib import admin
from. models import pincode



class Adminpincode(admin.ModelAdmin):
    list_display = ['pincode','city']
admin.site.register(pincode,Adminpincode)