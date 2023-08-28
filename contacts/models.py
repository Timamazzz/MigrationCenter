from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=60, blank=True)
    address = models.CharField(max_length=256, blank=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.name


class Manager(models.Model):
    post = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    image = models.ImageField(upload_to='images/managers/')

    class Meta:
        verbose_name = 'Руководитель'
        verbose_name_plural = 'Руководители'

    def __str__(self):
        return self.first_name + self.middle_name + self.surname
