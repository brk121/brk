# Generated by Django 4.1.7 on 2023-10-16 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('briansclub', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='table',
        ),
    ]