# Generated by Django 4.1.5 on 2023-03-08 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_information_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='date',
            field=models.DateField(default=datetime.date(2023, 3, 8)),
        ),
    ]
