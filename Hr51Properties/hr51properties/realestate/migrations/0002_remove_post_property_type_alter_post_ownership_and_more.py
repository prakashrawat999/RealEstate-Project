# Generated by Django 4.2 on 2023-05-06 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='property_type',
        ),
        migrations.AlterField(
            model_name='post',
            name='ownership',
            field=models.CharField(choices=[('1', 'first_ownership'), ('2', 'second_ownership'), ('3', 'third_ownership'), ('4', 'multiple_ownership')], max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='property_room',
            field=models.CharField(choices=[('1', '1BHK'), ('2', '2BHK'), ('3', '3BHK'), ('4', '4BHK'), ('5', '5BHK'), ('6', '6BHK'), ('7', '7BHK')], max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='property_status',
            field=models.CharField(choices=[('1', 'available for sell'), ('2', 'available for rent/lease'), ('3', 'not available')], max_length=30),
        ),
    ]
