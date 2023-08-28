import datetime
import os
from django.db import models


def get_news_gallery_path(instance, filename):
    if instance.news is None:
        return os.path.join('images/posts', str(1 if Post.objects.last() is None else Post.objects.last().id + 1),
                            'gallery', filename)
    else:
        return os.path.join('images/posts', str(instance.news.id), 'gallery', filename)


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
    previewImage = models.ImageField(upload_to=get_news_preview_path)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return str(self.date)


class PostImage(models.Model):
    image = models.ImageField(upload_to=get_news_gallery_path)
    news = models.ForeignKey(Post, on_delete=models.CASCADE)
