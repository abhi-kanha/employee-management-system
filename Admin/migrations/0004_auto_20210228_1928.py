# Generated by Django 3.1.6 on 2021-02-28 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_auto_20210221_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userType',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Admin', 'Admin'), ('Employee', 'Employee'), ('HR', 'HR')], default='Public', max_length=15),
        ),
    ]
