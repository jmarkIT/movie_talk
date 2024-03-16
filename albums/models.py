from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Album(models.Model):
    slug = models.CharField()
    title = models.CharField()
    artist = models.CharField()
    genres = ArrayField(base_field=models.CharField())

    def __str__(self):
        return self.title
