from django.db import models

# Create your models here.


class Subject(models.Model):
    code = models.CharField(max_length=100, blank=True)
    name_en = models.CharField(max_length=100, blank=True)
    url = models.URLField()

