# Generated by Django 3.1.6 on 2021-04-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0023_timesheet_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveapplication',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
