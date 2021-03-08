from django.urls import path
from . import views

urlpatterns = [

    path('order-lunch/',views.lunch,name = 'lunch'),
]