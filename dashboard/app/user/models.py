from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    email = models.EmailField(blank=True)
    date_joined = models.DateField()
    about = models.TextField(blank=True)
