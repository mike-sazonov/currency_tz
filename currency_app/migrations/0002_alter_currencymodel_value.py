# Generated by Django 5.1.1 on 2024-10-08 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencymodel',
            name='value',
            field=models.FloatField(),
        ),
    ]
