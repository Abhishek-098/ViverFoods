from django.shortcuts import render,redirect
from breakfast.models import product

# Create your views here.

def snacks(request):
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

        print(request.session['cart'])

        return redirect('snacks')

    if request.method =='GET':
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}

        prod = product.objects.all()
        
        return render(request, 'snacks.html',{'prod':prod})
