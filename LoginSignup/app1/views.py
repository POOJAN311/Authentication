from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def Homepage(request):
    current_user = request.session['user']
    param = {'current_user': current_user}
    return render(request, 'home.html', param)

def SignupPage(request):
    if request.method=='POST':
        uname= request.POST.get('username')
        email= request.POST.get('email')
        pass1= request.POST.get('password1')
        pass2= request.POST.get('password2')
        
        if pass1!=pass2:
            data="Passwords don't match"
            context={
                'data':data
            }
            return render(request, 'signup.html',context)
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)

        if user is not None:
             login(request,user)
             request.session['user'] = username
             return redirect('home')
        else:
            data="Username or Passwords is incorrect !"
            context={
                'data':data
            }
            return render(request, 'login.html',context)
        
    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')