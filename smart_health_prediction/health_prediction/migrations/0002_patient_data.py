# Generated by Django 3.0.8 on 2021-01-31 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_prediction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
