from django.db import models

# Create your models here.

class Photo(models.Model):
    image = models.URLField()
    author = models.CharField(max_length=255)

