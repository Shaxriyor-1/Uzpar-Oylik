# Generated by Django 4.2.3 on 2023-07-27 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0002_employeereport_department_employeereport_fee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeereport',
            name='month',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employeereport',
            name='year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
