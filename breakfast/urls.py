from django.urls import path
from . import views

urlpatterns = [

    path('order-breakfast/',views.breakfast, name = 'home'),
]