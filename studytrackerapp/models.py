from django.db import models

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    class Meta:
        app_label = 'studytrackerapp'  # Specify the app_label for this model

class Project(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    class Meta:
        app_label = 'studytrackerapp'  # Specify the app_label for this model

class Test(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    class Meta:
        app_label = 'studytrackerapp'  # Specify the app_label for this model