from django.contrib import admin
from .models import FilmModel, Review

admin.site.register(FilmModel)
admin.site.register(Review)
