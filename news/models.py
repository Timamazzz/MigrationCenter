import datetime
from django.db import models


# Create your models here.
class Post(models.Model):
    header = models.CharField(max_length=256)
    text = models.TextField()
    date = models.DateField(default=datetime.date.today())
    bannerImage = models.ImageField(upload_to='images/posts/%y/%m/%d/banner/', blank=True)
    bannerHeader = models.CharField(max_length=256, blank=True)
    bannerText = models.TextField(blank=True)
    previewImage = models.ImageField(upload_to='images/posts/%y/%m/%d/preview/')


class PostImage(models.Model):
    image = models.ImageField(upload_to='images/posts/%y/%m/%d/gallery/')
    news = models.ForeignKey(Post, on_delete=models.CASCADE)

