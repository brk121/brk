# Generated by Django 4.1.7 on 2023-10-22 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('briansclub', '0004_remove_order_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='table',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]