# Generated by Django 3.0.5 on 2021-02-02 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='standard',
            field=models.CharField(default='none', max_length=20),
            preserve_default=False,
        ),
    ]