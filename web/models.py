from django.db import models


# Create your models here.

class WORKER(models.Model):
    name = models.IntegerField(blank=False)