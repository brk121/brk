# Generated by Django 4.1.7 on 2023-10-22 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('briansclub', '0003_order_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='table',
        ),
    ]
