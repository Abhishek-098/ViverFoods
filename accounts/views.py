from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import pincode
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your views here.

def check(request):
    if request.method == 'POST':
        pc =pincode.objects.all( ) 
        print(pc)

        pin = request.POST['pcode']
        

        all_pins = []
        for p in pc:
            all_pins.append(p.pincode)
        if len(pin)<6 or len(pin)>6 or pin.isdigit()==False:
            messages.success(request,"Enter valid pincode")
            return redirect('register')
        if int(pin) in all_pins:
            messages.success(request,"yeyyy!  we are here")
            return redirect('register')
        else:
            #print('oooooooooooooooooooooooooooppppppppppppppppps')
            messages.success(request,"sorry! we are unavailable")
            return redirect('register')

        


        



def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email_id = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['cpassword']
        try:
            validate_email(email_id)
        except ValidationError as e:
            #print("bad email, details:", e)
            messages.success(request,'Please enter valid email id !!!')
            return redirect('register')
        else:
            print("good email")

        if first_name == '' or last_name == '' or email_id == '' or username =='' or password1 =='':
            messages.success(request,'All these are required fields !!!')
            return redirect('register')
        if User.objects.filter(email=email_id).exists():
            print('email already used with some account')
            messages.success(request,'Account already exists with this email id !!!')
            return redirect('register')
        if User.objects.filter(username = username).exists():
            print('username taken')
            messages.success(request,'Username taken !!!')
            return redirect('register')
            
        elif password1 != password2:
            print("Both Passwords must be same")
            return redirect('register')
        else:
            user = User.objects.create_user(username = username,password = password1,email = email_id, first_name = first_name,last_name = last_name,)
            user.save()
            return redirect('login')
    else:
        return render(request,'signup.html')




def login(request):

    if request.method == 'POST':
        




        username = request.POST['username']
        password = request.POST['password']


        user_auth_username = auth.authenticate(username = username ,password = password)
        #print("jasbdkkkssssssssssssssssssssssssssssss",user_auth_username)
        if user_auth_username is not None:
            user = user_auth_username
        else:
            val = User.objects.all()
            count_user =1
            for x in val:
                if username == x.email:
                    user = auth.authenticate(username = x.username,password = password)
                    count_user  =2
            if count_user == 1:
                user = None
        


        if user is not None:
            auth.login(request,user)
            request.session['user_id'] = user.id
            print(request.session.get('cart'))
            if request.session.get('cart') == None or request.session.get('cart') == {}:
                
                return redirect('/')
            else:
                return redirect('cart')

        else:
            messages.success(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'signin.html')

            


@cache_control(no_cache=True, must_revalidate=True)
def logout(request):
    c_cart = request.session.get('cart')
    
    
        
    request.session.flush()

    auth.logout(request)
    return redirect('/')
