from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterForm

# Create your views here.
def register_user(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username').capitalize()
            messages.success(request, f'Accound created for {username}')
            return redirect('event_list')
    return render(request, 'members/register.html',{
        'form': form, 
    })


def login_user(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('event_list')
    return render(request, 'members/login.html',{})

def logout_user(request):
    logout(request)
    return redirect('/')