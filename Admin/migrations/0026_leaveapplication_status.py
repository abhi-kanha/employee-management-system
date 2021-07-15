# Generated by Django 3.1.7 on 2021-04-16 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0025_auto_20210416_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveapplication',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20),
        ),
    ]
