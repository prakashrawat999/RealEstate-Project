# Generated by Django 4.2 on 2023-05-06 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0005_alter_property_ownership_alter_property_rooms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='ownership',
            field=models.CharField(choices=[('1', 'First Owner'), ('2', 'Second Owners'), ('3', 'Third Owners'), ('4', 'Multiple Owners')], max_length=15),
        ),
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.CharField(choices=[('1', 'For Sell'), ('2', 'For Rent/lease'), ('3', 'Not Available')], max_length=15),
        ),
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('1', 'Semi Furnished'), ('2', 'Fully Furnished'), ('3', 'Luxury'), ('4', 'Basic')], max_length=50),
        ),
    ]
