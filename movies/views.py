from django.shortcuts import render
from django.views import generic
from .models import Movie


# Create your views here.
class IndexView(generic.ListView):
    template_name = "movies/index.html"
    context_object_name = "list_of_movies"

    def get_queryset(self):
        return Movie.objects.order_by("title")


class DetailView(generic.DetailView):
    model = Movie
    template_name = "movies/detail.html"
