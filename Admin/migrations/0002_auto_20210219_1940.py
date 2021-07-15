# Generated by Django 3.1.6 on 2021-02-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='contact_No',
            new_name='card_no',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='address',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profilePicture',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cvc',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='state',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='userType',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Admin', 'Admin'), ('Public', 'Public')], default='Public', max_length=15),
        ),
    ]