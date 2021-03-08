from django.contrib import admin
from . models import product

# Register your models here.

class Adminproduct(admin.ModelAdmin):
    list_display = ['name','price','category','offer','offer_price','price_before']
admin.site.register(product,Adminproduct)

