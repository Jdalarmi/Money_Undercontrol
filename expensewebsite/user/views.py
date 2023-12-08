from django.shortcuts import render

def user_finance(request):
    return render(request, 'user_finance.html')

def register_user_finance(request):
    return render(request, 'register.html')