# Generated by Django 5.0 on 2023-12-12 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyfinance', '0007_month_payment_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month',
            name='payment_number',
            field=models.FloatField(default=0, null=True),
        ),
    ]
