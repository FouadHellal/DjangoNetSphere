# Generated by Django 4.2.7 on 2023-12-23 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_humidity_preassure'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='MyClubUser',
        ),
        migrations.DeleteModel(
            name='Venue',
        ),
    ]
