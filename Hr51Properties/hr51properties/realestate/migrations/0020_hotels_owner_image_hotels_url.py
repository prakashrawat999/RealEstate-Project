# Generated by Django 4.2 on 2023-05-16 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0019_hotels_add_date_alter_hotels_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='owner_image',
            field=models.ImageField(null=True, upload_to='user/'),
        ),
        migrations.AddField(
            model_name='hotels',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
