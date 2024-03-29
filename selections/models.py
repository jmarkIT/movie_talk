from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Selection(models.Model):
    movie = models.ForeignKey(
        "Movie",
        on_delete=models.CASCADE,
    )
    album = models.ForeignKey(
        "Album",
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    owner = models.CharField()

    def __str__(self):
        return self.get_title()

    def get_title(self):
        return f"{self.movie.title} & {self.album.title}"


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


class Album(models.Model):
    slug = models.CharField()
    title = models.CharField()
    artist = models.CharField()
    genres = ArrayField(base_field=models.CharField())

    def __str__(self):
        return self.title
