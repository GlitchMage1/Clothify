from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Пароли должны совпадать!')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует')
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        login(request, user)
        return redirect('index')

    return render(request, 'user/signup.html')
