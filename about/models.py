from django.db import models


# Create your models here.
class Document(models.Model):
    Additional_activity = 'Additional_activity'
    AreaOfActivity = 'AreaOfActivity'
    Regulation = 'Regulation'
    Other = 'Other'
    types = (
        (Additional_activity, 'Дополнительные виды деятельности'),
        (AreaOfActivity, 'Направления деятельности'),
        (Regulation,
         'Уставные документы Автономной Некоммерческой организации «Центр помощи, поддержки, социальной и трудовой '
         'адаптации»'),
        (Other, 'Прочие ДОКУМЕНТЫ')
    )
    name = models.CharField(max_length=256)
    text = models.TextField()
    type = models.CharField(max_length=256, choices=types)
    previewImage = models.ImageField(upload_to='images/docs/%y/%m/%d',
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