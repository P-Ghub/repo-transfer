from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from . import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your views here.
def authenticate_user(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:store_login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('store:home_page')
    )

def create_user(request):
    if request.method == 'POST':
        form = models.RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']     
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            User.objects.create_user(username=username, password=password, first_name=first_name)
            return render(request, 'store_templates/successful_reg.html', {})  
    else:
        form = models.RegistrationForm()
    return render(request, 'user_templates/create_user.html', {'form': form})

def store_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('store:successful_order')
        
        else:
            return redirect('user_auth:store_login') 

    return render(request, 'user_templates/store_login.html', {})
