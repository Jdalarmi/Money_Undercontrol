# Generated by Django 5.0 on 2023-12-08 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyfinance', '0004_alter_month_value_all'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month',
            name='value_all',
            field=models.FloatField(),
        ),
    ]
