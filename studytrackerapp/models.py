from django.db import models
from django.contrib.auth.models import User
class Assignment(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    class Meta:
        app_label = 'studytrackerapp'  

class Project(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    class Meta:
        app_label = 'studytrackerapp'  

class Test(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    class Meta:
        app_label = 'studytrackerapp'  

    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
