from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages

def user_finance(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuario não existe! Favor registre seu usuario.')
            return redirect('user_finance')
    return render(request, 'user_finance.html')

def register_user_finance(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if len(username) < 4:
            messages.error(request, "Por favor insira usuario com mais de 4 caracteres")
            return redirect('register-user-finance')
        for i in username:
            if i.isdigit():
                messages.error(request, "Nome de usuario não pode conter numeros!")
                return redirect('register-user-finance')
        if len(password) < 8:
            messages.error(request, "Favor insira senha maior que 8 digitos!")
            return redirect('register-user-finance')
        user = User.objects.create_user(
            username=username,
            password=password
            )
        print(user)

        user.save() 
        return redirect('user_finance')
    return render(request, 'register.html')

def logout_user_finance(request):
    auth.logout(request)

    return redirect('user_finance')