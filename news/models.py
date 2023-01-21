from django.db import models


# Create your models here.
class News(models.Model):
    header = models.CharField(max_length=256)
    text = models.TextField()
    image = models.ImageField()
