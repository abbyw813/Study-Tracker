from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.mail import send_mail
from .models import Assignment, Project, Test, Assignment_Rem, Project_Rem, Test_Rem

@receiver(pre_save, sender=Assignment)
@receiver(pre_save, sender=Project)
@receiver(pre_save, sender=Test)
def set_reminder(sender, instance, **kwargs):
    reminder_date = instance.due_date - timezone.timedelta(days=1)  # Set reminder 1 day before due date
    
    if sender == Assignment:
        Assignment_Rem.objects.create(title=instance.title, due_date=reminder_date, description='Reminder for assignment')
    elif sender == Project:
        Project_Rem.objects.create(title=instance.title, due_date=reminder_date, description='Reminder for project')
    elif sender == Test:
        Test_Rem.objects.create(title=instance.title, due_date=reminder_date, description='Reminder for test')