from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from .forms import LoginForm, RegisterForm


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('user_page')
            else:
                form.add_error('username', 'Credentials are not valid')
    context = {
        'form': form,
        'auth' : True
    }
    return render(request, 'users/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def registration_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if (form.is_valid() and 
            form.cleaned_data['password'] == form.cleaned_data['password1']):
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                form.add_error(
                    'username',
                    'User with such email is already exsists'
                )
            else:
                user = User.objects.create(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                )
                user.set_password(form.cleaned_data['password'])
                user.save()
                return redirect('login')
    context = {
        'form': form,
        'auth': True
    }
    return render(request, 'users/registration.html', context)

