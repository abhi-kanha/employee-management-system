# Generated by Django 3.1.6 on 2021-03-07 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_auto_20210307_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='contact_No',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
