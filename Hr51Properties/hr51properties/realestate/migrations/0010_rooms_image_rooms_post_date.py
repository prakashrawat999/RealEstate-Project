# Generated by Django 4.2 on 2023-05-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0009_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='image',
            field=models.ImageField(null=True, upload_to='post/'),
        ),
        migrations.AddField(
            model_name='rooms',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
