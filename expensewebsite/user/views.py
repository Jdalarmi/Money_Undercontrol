from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User

def user_finance(request):
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
        return redirect('user_finance')
    return render(request, 'register.html')