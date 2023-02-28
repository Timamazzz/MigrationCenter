# Generated by Django 4.1.5 on 2023-02-18 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_post_bannerimage_alter_post_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bannerImage',
            field=models.ImageField(blank=True, upload_to='news/images/posts/%y/%m/%d/banner/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='previewImage',
            field=models.ImageField(upload_to='news/images/posts/%y/%m/%d/preview/'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(upload_to='news/images/posts/%y/%m/%d/list/'),
        ),
    ]