from django.contrib import admin
from .models import Album, Movie, Selection

# Register your models here.

admin.site.register(Selection)
admin.site.register(Movie)
admin.site.register(Album)
