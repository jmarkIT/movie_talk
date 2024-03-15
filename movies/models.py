from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Movie(models.Model):
    slug = models.CharField()
    title = models.CharField()
    director = models.CharField()
    cinematographer = models.CharField()
    writer = ArrayField(base_field=models.CharField())
    genre = ArrayField(base_field=models.CharField())
    just_watch_link = models.CharField("JustWatch Link")
    wiki_link = models.CharField("Wikipedia Link")
    imdb_link = models.CharField("IMDB Link")

    def __str__(self):
        return self.title
