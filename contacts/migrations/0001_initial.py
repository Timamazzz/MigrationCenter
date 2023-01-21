# Generated by Django 4.1.5 on 2023-01-20 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=256)),
                ('first_name', models.CharField(max_length=256)),
                ('middle_name', models.CharField(max_length=256)),
                ('surname', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
