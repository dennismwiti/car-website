# Generated by Django 4.2.4 on 2023-08-16 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_car_doors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand_slug',
            field=models.SlugField(default='', max_length=200),
        ),
    ]
