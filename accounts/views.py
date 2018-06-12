from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate 
from django.http import HttpResponse
from .forms import UserLoginForm
# Create your views here.
def login(request):
    if request.method =="POST":
        u=request.POST['username'] 
        p=request.POST['password']
        user = authenticate(username=u, password=p)
        
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else: 
            return HttpResponse("That user or passwordis wrong")
    else:
        login_form = UserLoginForm()
        return render (request, 'accounts/login.html', {'form': login_form})
    
def register(request):
    return render(request, 'accounts/register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')