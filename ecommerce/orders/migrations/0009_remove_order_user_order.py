# Generated by Django 2.1.7 on 2019-05-11 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20190511_0244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user_order',
        ),
    ]