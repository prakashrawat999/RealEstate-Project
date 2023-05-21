# Generated by Django 4.2 on 2023-05-21 05:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0023_alter_reservation_check_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='is_published',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='rooms',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]