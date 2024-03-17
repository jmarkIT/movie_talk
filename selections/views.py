from django.shortcuts import render
from django.views import generic
from .models import Album, Movie, Selection


# Create your views here.


# Album Views
class AlbumIndexView(generic.ListView):
    template_name = "albums/index.html"
    context_object_name = "list_of_albums"

    def get_queryset(self):
        return Album.objects.order_by("title")


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = "albums/detail.html"


# Movies Views
class MovieIndexView(generic.ListView):
    template_name = "movies/index.html"
    context_object_name = "list_of_movies"

    def get_queryset(self):
        return Movie.objects.order_by("title")


class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = "movies/detail.html"
