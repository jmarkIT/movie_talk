from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Album, Movie, Selection


# Create your views here.


# Selection Views
class IndexView(generic.ListView):
    template_name = "selections/index.html"
    context_object_name = "list_of_selections"

    def get_queryset(self) -> QuerySet[Any]:
        return Selection.objects.order_by("date")


class DetailView(generic.DetailView):
    model = Selection
    template_name = "selections/detail.html"


# Album Views
class AlbumIndexView(generic.ListView):
    template_name = "selections/albums/index.html"
    context_object_name = "list_of_albums"

    def get_queryset(self):
        return Album.objects.order_by("title")


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = "selections/albums/detail.html"


# Movies Views
class MovieIndexView(generic.ListView):
    template_name = "selections/movies/index.html"
    context_object_name = "list_of_movies"

    def get_queryset(self):
        return Movie.objects.order_by("title")


class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = "selections/movies/detail.html"
