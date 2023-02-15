import datetime

from django.db import models


# Create your models here.
class News(models.Model):
    header = models.CharField(max_length=256)
    text = models.TextField()
    date = models.DateField(default=datetime.date.today())


class NewsImage(models.Model):
    image = models.ImageField(upload_to='images/news/')
    news = models.ForeignKey(News, on_delete=models.CASCADE)


class SliderImage(models.Model):
    image = models.ImageField(upload_to='images/slider/')
