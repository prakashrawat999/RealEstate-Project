# Generated by Django 4.2 on 2023-05-23 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0024_rooms_is_published_rooms_list_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hotels',
            new_name='Realator',
        ),
    ]
