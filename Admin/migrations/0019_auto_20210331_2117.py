# Generated by Django 3.1.6 on 2021-03-31 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0018_resultpublish'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resultpublish',
            old_name='sname',
            new_name='ename',
        ),
    ]