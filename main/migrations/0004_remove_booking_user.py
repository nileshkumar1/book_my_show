# Generated by Django 2.2 on 2019-05-13 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_booking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
    ]