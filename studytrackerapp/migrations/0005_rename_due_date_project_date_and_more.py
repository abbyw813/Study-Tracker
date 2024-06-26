# Generated by Django 4.2.7 on 2024-04-14 21:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studytrackerapp', '0004_rename_due_date_test_date_remove_test_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='due_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='project',
            name='title',
        ),
        migrations.AddField(
            model_name='project',
            name='subject',
            field=models.CharField(default=datetime.datetime(2024, 4, 14, 21, 26, 26, 708753, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
    ]
