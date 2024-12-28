from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from menus.models import Dish
# Create your views here.

def home(request):
    new_dishes = Dish.objects.all()[0:8]
    return render(request, 'home.html', {'new_dishes': new_dishes})

def loginview(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request, username=uname, password=pwd)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return render(request,"login.html",{"msg":"Invalid login"})


def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):
    try:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():   
                form.save() 
                return redirect('login')
            messages.error(request, 'registration/signup.html')
            return render(request, 'registration/signup.html', {'form': form,'msg':'Invalid details'})       
        else:
            form=UserCreationForm()
            return render(request, 'registration/signup.html', {'form': form})
    except Exception as e:
            print(e)
            userform = UserCreationForm()
            return render(request, 'registration/signup.html', {'form': form})
    
def passwordreset(request):
    if request.method == "POST":
        uname = request.POST['username']
        newpwd1=request.POST['password1']
        newpwd2=request.POST['password2']
        try:
            if newpwd1 == newpwd2:
                user=User.objects.get(username=uname)
                if user is not None:
                    user.set_password(newpwd1)
                    user.save()
                return render(request,"registration/ResetPassword.html",{"msg":"Password Reset Successfull"})
            else:
                return render(request,"registration/ResetPassword.html",{"msg":"Passwords do not match"})
        except Exception as e:
            print(e)
            return render(request,"registration/ResetPassword.html",{"msg":"Password Reset Failed"})
    return render(request,'registration/ResetPassword.html')
