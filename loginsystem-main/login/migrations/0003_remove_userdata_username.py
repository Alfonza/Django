# Generated by Django 3.1.5 on 2021-01-20 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20210120_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='username',
        ),
    ]