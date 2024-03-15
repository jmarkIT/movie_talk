from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Movie(models.Model):
    title = models.CharField()
    director = models.CharField()
    cinematographer = models.CharField()
    writer = ArrayField(base_field=models.CharField())
    genre = ArrayField(base_field=models.CharField())
    just_watch_link = models.CharField()
    wiki_link = models.CharField()
    imdb_link = models.CharField()
