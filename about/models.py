from django.db import models


# Create your models here.
class AreaOfActivity(models.Model):
    header = models.CharField(max_length=256)
    text = models.TextField()
    image = models.ImageField()


class History(models.Model):
    header = models.CharField(max_length=256)
    text = models.TextField()


class TypeOfDocument(models.Model):
    name = models.CharField(max_length=256)


class Document(models.Model):
    name = models.CharField(max_length=256)
    text = models.TextField()
    type = models.ForeignKey(TypeOfDocument, on_delete=models.CASCADE)


class Vacancy(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField()
    requirements = models.TextField()
    experience = models.TextField()
    conditions = models.TextField()
    wages = models.FloatField()

