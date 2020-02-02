from django.db import models

from django.utils import timezone


class Police(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    USERNAME_FIELD = 'email'
    date_registered = models.DateTimeField(default=timezone.now)
    branch = models.CharField(max_length=30, blank=False)
    post = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return f'police - ' + self.email
