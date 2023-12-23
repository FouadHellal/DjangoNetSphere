# Generated by Django 4.2.7 on 2023-12-08 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_ipaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('temperature', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='IPAddress',
        ),
    ]