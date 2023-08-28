from django.db import models


# Create your models here.
class InsuranceService(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    subtext = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Услуга страхования'
        verbose_name_plural = 'Услуги страхования'

    def __str__(self):
        return self.name
