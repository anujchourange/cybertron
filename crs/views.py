from django.shortcuts import render
from django.http import HttpResponse
from report.models import report
from User.models import User
from police.models import Police


def about(request):
    return render(request, 'crs/about.html', {'title': 'About'})


def index(request):
    
    context = {
        'users': User.objects.all()
    }
    return render(request, 'crs/index.html', context)
