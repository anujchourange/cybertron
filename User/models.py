from django.db import models
from django.utils import timezone


class User(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    USERNAME_FIELD = 'email'
    password = models.CharField(default=1234568,  max_length=50)
    date_registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
