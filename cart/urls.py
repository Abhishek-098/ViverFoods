from django.urls import path
from . import views

urlpatterns = [

    path('your-cart',views.showcart,name ='cart'),
    path('item-plus',views.plus,name = 'item-plus'),
    path('item-minus',views.minus,name = 'item-minus'),
    path('checkout',views.checkout,name = 'checkout'),
    path('status',views.order_status,name = 'status'),

]