# Generated by Django 4.1.5 on 2023-08-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='insuranceservice',
            name='subtext',
            field=models.TextField(blank=True, null=True),
        ),
    ]
