from django.urls import path

from . import views

app_name = "selections"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("selection/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("movies/", views.MovieIndexView.as_view(), name="movies_index"),
    path("movies/<str:slug>/", views.MovieDetailView.as_view(), name="movies_detail"),
    path("albums/", views.AlbumIndexView.as_view(), name="albums_index"),
    path("albums/<str:slug>/", views.AlbumDetailView.as_view(), name="albums_detail"),
]
