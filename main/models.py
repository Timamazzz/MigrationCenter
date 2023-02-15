from django.db import models


# Create your models here.
class Information(models.Model):
    header = models.CharField(max_length=256)
    text = models.TextField()


class FrequentQuestions(models.Model):
    header = models.CharField(max_length=256)
    text = models.TextField()


class BannerInfo(models.Model):
    header = models.CharField(max_length=256)
    text = models.TextField()
    image = models.ImageField()
