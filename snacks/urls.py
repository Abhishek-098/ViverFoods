from django.urls import path
from . import views

urlpatterns = [
    path('order-snacks/',views.snacks,name = 'snacks'),
]