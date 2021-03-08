from django.shortcuts import render,redirect
from breakfast.models import product
from django.contrib .auth.models import User,auth
from index.models import orders
from accounts.models import pincode
from django.contrib import messages
from index.models import orders

# Create your views here.

def order_status(request):
    user = request.user
    #print(user.id)
    Orders = orders.objects.all().order_by('-date')
   
    #print(Orders)
    items =[]
    count =0
    for ord in Orders:
        if count<15:
            if user == ord.customer:
                items.append(ord)
                count+=1
        else:
            break
            
            
    

    

            


    return render(request,'status.html',{'items':items})




def checkout(request):
    if request.method == 'POST':
        user = request.user
    #print(user)
        users = User.objects.all()
        if user not in users:
            return redirect('login')

        else:
            house = request.POST['house_number']
            city = request.POST['city']
            phone = request.POST['phone']
            pin_code = request.POST['pincode']

            user = request.user

            pin = pincode.objects.all()
            all_pins = []
            for p in pin:
                all_pins.append(p.pincode)
            #print(all_pins)
        


            
            if int(pin_code) in all_pins:
            
                cart = request.session.get('cart')
                ids = list(request.session.get('cart').keys())
                products = product.objects.filter(id__in = ids) 
            # print(products)
            # print(cart)
                
                for prod in products:
                    quant = cart.get(str(prod.id))
                    order = orders(customer = user,
                                    product = prod,
                                    
                                    quantity = cart.get(str(prod.id)),
                                    price = (prod.price*quant),
                                    landmark = house,
                                    city = city,
                                    pincode = pin_code,
                                    phone = phone)
                    order.save()
                    request.session['cart'] = {}
                    messages.success(request,'Order placed successfully 😊')
            else:
                #print('We are in else part')
                messages.success(request,"Sorry we are not available at this pincode")
                #return redirect ('cart')
                


                


        

            return redirect('cart')
            


def plus(request):
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
    return redirect('cart')

def minus(request):
    if  request.method =='POST':
        pid = request.POST['pId']
        remove = request.POST.get('remove')
        print(remove)
        #print(pid)
        cart = request.session.get('cart')
        
        if cart:

            quantity = cart.get(pid)
            
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(pid)
                    else:
                        cart[pid] = quantity-1
           # else:
            #    cart[pid] = 1
       # else:
        #    cart = {}
         #   cart[pid] = 1
        
        request.session['cart'] = cart

        #print(request.session['cart'])

    return redirect('cart')


        
                

        
                



def showcart(request):
    
    cart = request.session.get('cart')
            #print(cart)
    if not cart:
       request.session['cart'] = {}
        
    ids = list(request.session.get('cart').keys())
    products = product.objects.filter(id__in = ids)
    #print(products)
        

        #for p in products:
            #print(p.id)
            
        #print(request.session.get('cart').values())
        #print(request.session.get('cart'))

            
            

        
    return render(request,'cart.html',{'products' : products })