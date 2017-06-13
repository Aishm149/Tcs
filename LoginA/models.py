from django.db import models
from django.utils import timezone


class Profile(models.Model):
    userID = models.ForeignKey('auth.User')
    userName = models.CharField(max_length=20, unique=True)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)

