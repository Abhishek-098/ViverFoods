from django.urls import path
from . import views

urlpatterns = [
    path('orderdesserts/',views.dess,name = 'desserts'),
]