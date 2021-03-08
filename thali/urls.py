from django.urls import path 
from . import views

urlpatterns =[

    path('orderthali/',views.thali,name = 'thali'),
    
]