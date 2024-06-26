# Generated by Django 4.1.7 on 2023-10-22 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('briansclub', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='table',
        ),
        migrations.CreateModel(
            name='OrdersNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('orders', models.ManyToManyField(related_name='orders_number', to='briansclub.order')),
            ],
        ),
    ]
