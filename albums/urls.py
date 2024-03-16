from django.urls import path

from . import views

app_name = "albums"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<str:slug>/", views.DetailView.as_view(), name="detail"),
]
