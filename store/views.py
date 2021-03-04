from django.shortcuts import render, redirect

from store.forms import CustomSignUpForm


def index(request):
    return render(request=request, template_name='store/index.html', context={})


def signup_page(request):
    return render(request=request, template_name='store/register.html', context={})


def signup(request):
    if request.method == 'POST':
        signup_form = CustomSignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
        return redirect('home_page')
