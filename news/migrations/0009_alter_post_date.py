# Generated by Django 4.1.5 on 2023-02-22 01:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_post_bannerimage_alter_post_previewimage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date(2023, 2, 22)),
        ),
    ]
