from django.shortcuts import render
from django.views import generic
from .models import Album


# Create your views here.
class IndexView(generic.ListView):
    template_name = "albums/index.html"
    context_object_name = "list_of_albums"

    def get_queryset(self):
        return Album.objects.order_by("title")


class DetailView(generic.DetailView):
    model = Album
    template_name = "albums/detail.html"
