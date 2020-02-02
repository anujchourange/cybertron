from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
import json
from .models import User
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            # Encrypted Password in database
            password = make_password(password)
            phone_number = form.cleaned_data.get('phone_number')

            user_data = User(fname=fname, lname=lname,
                             email=email, phone_number=phone_number, password=password)
            user_data.save()
            messages.success(request, f'Account created for {email}!')
            return redirect('crs-home')
    # if request.method == "POST":
    #     #form = UserCreationForm(request.POST)
    #     fname = request.POST['fname']
    #     lname = request.POST['lname']
    #     email = request.POST['email']
    #     phone_number = request.POST['phone_number']
    #     password = request.POST['password']

    #     user = User(fname=fname, lname=lname, email=email,
    #                 phone_number=phone_number)
    #     user.save()
    else:
        form = UserRegisterForm()
    return render(request, 'User/register.html', {'form': form})
