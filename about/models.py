import os

from django.db import models


def get_docs_preview_path(instance, filename):
    if instance.pk is None:
        return os.path.join('images/docs',
                            str(1 if Document.objects.last() is None else Document.objects.last().id + 1),
                            'preview', filename)
    else:
        return os.path.join('images/docs', str(instance.pk), 'preview', filename)


def get_news_gallery_path(instance, filename):
    if instance.document is None:
        return os.path.join('images/docs',
                            str(1 if Document.objects.last() is None else Document.objects.last().id + 1),
                            'gallery', filename)
    else:
        return os.path.join('images/docs', str(instance.document.id), 'gallery', filename)


# Create your models here.
class Document(models.Model):
    Regulation = 'Regulation'
    Other = 'Other'
    Reporting = 'Reporting'
    types = (
        (Regulation,
         'Уставные документы Автономной Некоммерческой организации «Центр помощи, поддержки, социальной и трудовой '
         'адаптации»'),
        (Other, 'Прочие ДОКУМЕНТЫ'),
        (Reporting, 'Отчетность')
    )
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=256, choices=types)
    previewImage = models.ImageField(upload_to=get_docs_preview_path,
                                     default='images/docs/default_doc.png', blank=True)


class DocImage(models.Model):
    image = models.ImageField(upload_to=get_news_gallery_path)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)


class AdditionalActivity(models.Model):
    name = models.CharField(max_length=256)
    text = models.TextField()
    previewImage = models.ImageField(upload_to='images/AdditionalActivity/',
                                     default='images/docs/default_doc.png', blank=True)


class AreaOfActivity(models.Model):
    name = models.CharField(max_length=256)
    text = models.TextField()
    previewImage = models.ImageField(upload_to='images/AreaOfActivity/',
                                     default='images/docs/default_doc.png', blank=True)


class Vacancy(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='images/vacancy/%y/%m/%d',
                              default='images/vacancy/default_vac.png', blank=True)
    requirements = models.TextField()
    experience = models.TextField()
    conditions = models.TextField()
    wages = models.FloatField()
    is_active = models.BooleanField(default=True)
