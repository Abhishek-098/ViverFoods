from django.urls import path
from . import views

urlpatterns = [

    path('order-dinner/',views.dinner,name ='dinner'),
]