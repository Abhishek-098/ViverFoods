from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import product
from django.views import View

# Create your views here.


def breakfast(request):
    if  request.method =='POST':
        pid = request.POST['pId']
        #print(pid)
        cart = request.session.get('cart')
        
        if cart:

            quantity = cart.get(pid)
            if quantity:
                cart[pid] = quantity+1
            else:
                cart[pid] = 1
        else:
            cart = {}
            cart[pid] = 1
        
        request.session['cart'] = cart

        #print(request.session['cart'])


        return redirect('home')


    if request.method =='GET':

        cart = request.session.get('cart')
        
        if not cart:
            request.session.cart = {}
        
        
        prod = product.objects.all()
        
        return render(request, 'breakfast.html',{'prod':prod})