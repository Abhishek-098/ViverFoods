from django.shortcuts import render

# Create your views here.

def home(request):
    cart = request.session.get('cart')
    #print("this is your cart :",cart)
    if not cart:
        request.session.cart = {}
   # print('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO',request.session.get('user_id'))
    return render(request,'welcome.html')
