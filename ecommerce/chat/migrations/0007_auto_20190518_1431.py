# Generated by Django 2.1.7 on 2019-05-18 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_technicalsuppoertmessages_close'),
    ]

    operations = [
        migrations.RenameField(
            model_name='technicalsuppoertmessages',
            old_name='close',
            new_name='close_ticket',
        ),
    ]
