# Generated by Django 4.2.4 on 2023-08-28 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0014_alter_car_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='features',
            field=models.CharField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], null=True),
        ),
    ]