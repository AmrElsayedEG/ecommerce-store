# Generated by Django 2.1.7 on 2019-05-06 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.TextField(default='Null'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='tel',
            field=models.CharField(default='Null', max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='Null', max_length=10),
        ),
    ]
