from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from store.forms import CustomSignUpForm


def index(request):
    return render(request=request, template_name='store/index.html', context={})


def signup_page(request):
    if request.method == 'GET':
        return render(request=request, template_name='store/register.html', context={})
    if request.method == 'POST':
        signup_form = CustomSignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
        else:
            return render(request=request, template_name='store/register.html',
                          context={'error': dict(signup_form.errors.items())['__all__'][0]})
        return redirect('home_page')


def login_page(request):
    if request.method == 'GET':
        return render(request=request, template_name='store/login.html', context={})
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request=request, template_name='store/login.html',
                          context={'error': 'username is not valid'})
        else:
            if not user.check_password(password):
                return render(request=request, template_name='store/login.html',
                              context={'error': 'password is not valid'})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('success')
            return redirect('home_page')


def logout_user(request):
    logout(request)
    return redirect('home_page')
