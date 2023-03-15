import os
import datetime
from django.db import models
from news.models import Post


def get_news_banner_path(instance, filename):
    if instance.pk is None:
        return os.path.join('images/banner',
                            str(1 if MainBanner.objects.last() is None else MainBanner.objects.last().id + 1), filename)
    else:
        return os.path.join('images/banner', str(instance.pk), filename)


# Create your models here.
class Information(models.Model):
    header = models.CharField(max_length=256)
    text = models.TextField()
    date = models.DateField(default=datetime.date.today())


class FrequentQuestions(models.Model):
    header = models.CharField(max_length=256)
    text = models.TextField()


class MainBanner(models.Model):
    image = models.ImageField(upload_to=get_news_banner_path)
    header = models.CharField(max_length=256, blank=True)
    text = models.TextField(blank=True)
    link = models.CharField(max_length=2048, blank=True, null=True)
    date = models.DateField(default=datetime.date.today())
    is_active = models.BooleanField(default=True)
