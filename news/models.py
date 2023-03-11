import datetime
import os
from django.db import models


def get_news_gallery_path(instance, filename, sub_path):
    if instance.pk is None:
        return os.path.join('images/', str(1 if Post.objects.last() is None else Post.objects.last().id + 1),
                            'gallery', filename)
    else:
        return os.path.join('images/posts', str(instance.pk), 'gallery', filename)


def get_news_banner_path(instance, filename):
    if instance.pk is None:
        return os.path.join('images/posts', str(1 if Post.objects.last() is None else Post.objects.last().id + 1),
                            'banner', filename)
    else:
        return os.path.join('images/posts', str(instance.pk), 'banner', filename)


def get_news_preview_path(instance, filename):
    if instance.pk is None:
        return os.path.join('images/posts', str(1 if Post.objects.last() is None else Post.objects.last().id + 1),
                            'preview', filename)
    else:
        return os.path.join('images/posts', str(instance.pk), 'preview', filename)


# Create your models here.
class Post(models.Model):
    header = models.CharField(max_length=256)
    text = models.TextField()
    date = models.DateField(default=datetime.date.today())
    bannerImage = models.ImageField(upload_to=get_news_banner_path, blank=True)
    bannerHeader = models.CharField(max_length=256, blank=True)
    bannerText = models.TextField(blank=True)
    previewImage = models.ImageField(upload_to=get_news_preview_path)


class PostImage(models.Model):
    image = models.ImageField(upload_to=get_news_gallery_path)
    news = models.ForeignKey(Post, on_delete=models.CASCADE)
