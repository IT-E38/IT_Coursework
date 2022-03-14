from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    dob = models.DateField()
    description = models.CharField(max_length=255, blank=True)


class Video(models.Model):
    title = models.CharField(max_length=30)
    length = models.TimeField()
    Views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    tag = models.CharField(max_length=255)
    url = models.URLField()
    picture = models.ImageField(upload_to="video_picture")


class Manager(models.Model):
    manager = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    dob = models.DateField()
    description = models.CharField(max_length=255, blank=True)
