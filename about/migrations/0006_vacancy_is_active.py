# Generated by Django 4.1.5 on 2023-02-22 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_alter_vacancy_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
