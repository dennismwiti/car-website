# Generated by Django 4.2.4 on 2023-08-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contact_car_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='car_id',
            field=models.IntegerField(),
        ),
    ]