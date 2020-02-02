from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
import json
from .models import report as Report
from User.models import User
from django.contrib import messages
from .forms import ReportCrime
from django.utils import timezone
#from django.contrib.auth.hashers import make_password
from django.http import HttpResponse


def report(request):
    if request.method == 'POST':
        form = ReportCrime(request.POST, request.FILES)
        if form.is_valid():
            event_time = form.cleaned_data.get('event_time')
            # event_report =
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            image = form.cleaned_data.get('image')
            location_lat = form.cleaned_data.get('location_lat')
            location_lng = form.cleaned_data.get('location_lng')
            user_id = form.cleaned_data.get('user_id')
            try:

                user_id = User.objects.get(email=user_id)
                user_id = user_id.id
            except User.DoesNotExist:
                user_id = 0  # 0 for guest user i.e user does not exist
            # as email is sent from user as user id in user_id variable so                              $event_report=

            status = 0
            report_data = Report(event_time=event_time, image=image, location_lat=location_lat, location_lng=location_lng, status=status, title=title, description=description,
                                 user_id=user_id)
            report_data.save()

            # fname = form.cleaned_data.get('fname')
            # lname = form.cleaned_data.get('lname')
            # email = form.cleaned_data.get('email')
            # password = form.cleaned_data.get('password1')
            # # Encrypted Password in database
            # password = make_password(password)
            # phone_number = form.cleaned_data.get('phone_number')

            # user_data = User(fname=fname, lname=lname,
            #                  email=email, phone_number=phone_number, password=password)
            # user_data.save()

            messages.success(
                request, f'Report created for !')
            # HttpResponse('image upload success'),
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
        form = ReportCrime()
    return render(request, 'Reports/report.html', {'form': form})


def total_reports(request):
    if Report.objects.all():
        context = {
            'reports': Report.objects.all()
        }
    else:
        context = {
            'reports': {{'id': 1, 'title': "TITLE 1 Example", 'description': "Description 1 big described", 'event_time': 'August-21-2019', 'location': "19.1383,19.1383"},
                        {'id': 2, 'title': "TITLE 2 Example", 'description': "Description 2 big described",
                            'event_time': 'August-20-2019', 'location': "19.1383,19.1383"},
                        {'id': 3, 'title': "TITLE 3 Example", 'description': "Description 3 big described", 'event_time': 'August-20-2019', 'location': "19.1383,19.1383"}, }
        }
    return render(request, 'Reports/totalreport.html', context)
