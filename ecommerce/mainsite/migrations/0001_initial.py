# Generated by Django 2.1.7 on 2019-05-04 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Price', models.IntegerField()),
                ('Discount_Price', models.IntegerField(blank=True, null=True)),
                ('Details', models.TextField()),
                ('Information', models.TextField()),
            ],
        ),
    ]
