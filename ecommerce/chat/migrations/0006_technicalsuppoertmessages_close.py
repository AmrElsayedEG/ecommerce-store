# Generated by Django 2.1.7 on 2019-05-18 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_technicalsupportticket_is_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='technicalsuppoertmessages',
            name='close',
            field=models.BooleanField(default=False),
        ),
    ]
