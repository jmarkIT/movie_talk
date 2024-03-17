from django.urls import path

from . import views

app_name = "selections"
urlpatterns = [
    path("movies/", views.MovieIndexView.as_view(), name="index"),
    path("movies/<str:slug>/", views.MovieDetailView.as_view(), name="detail"),
    path("albums/", views.AlbumIndexView.as_view(), name="index"),
    path("albums/<str:slug>/", views.AlbumDetailView.as_view(), name="detail"),
]
