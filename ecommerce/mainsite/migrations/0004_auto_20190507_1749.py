# Generated by Django 2.1.7 on 2019-05-07 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_addproduct_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='Category',
            field=models.CharField(choices=[('Dresses', 'Dresses'), ('Blouses', 'Blouses'), ('T-shirts', 'T-shirts'), ('OutWare', 'OutWare'), ('Bags', 'Bags'), ('Other', 'Other')], default='Other', max_length=50),
        ),
    ]
