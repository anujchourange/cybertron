import re
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from User.models import User
import datetime
from django import forms


class report(models.Model):
    event_time = models.DateTimeField(auto_now_add=False)
    event_report = models.DateTimeField(editable=True, auto_now=True)
    image = models.ImageField(upload_to='report_images', height_field=None,
                              width_field=None, max_length=100, null=True, blank=True)
    location_lat = models.FloatField(null=False, blank=False)
    # models.models.DecimalField(max_digits=22, decimal_places=16)
    location_lng = models.FloatField(null=False, blank=False)
    status = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(null=True, max_length=100)
    user_id = models.EmailField(max_length=254, null=True)

    def __str__(self):
        return f"Report " + str(self.id)
