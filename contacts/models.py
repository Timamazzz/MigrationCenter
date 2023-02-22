from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)


class Manager(models.Model):
    post = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    image = models.ImageField(upload_to='images/managers/')
