from django.db import models
import datetime


# Create your models here.
class Information(models.Model):
    header = models.CharField(max_length=256)
    text = models.TextField()
    date = models.DateField(default=datetime.date.today())


class FrequentQuestions(models.Model):
    header = models.CharField(max_length=256)
    text = models.TextField()
