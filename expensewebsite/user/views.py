from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth

def user_finance(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
    return render(request, 'user_finance.html')

def register_user_finance(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            password=password
            )
        print(user)

        user.save() 
        return redirect('user-finance')
    return render(request, 'register.html')

def logout_user_finance(request):
    auth.logout(request)

    return redirect('user_finance')