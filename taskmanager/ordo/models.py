from django.db import models

# Create your models here.


class Ordo(models.Model):
    name = models.CharField(max_length=25)
