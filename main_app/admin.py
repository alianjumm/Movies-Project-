from django.contrib import admin
from .models import Movie, Watched, Actor

# Register your models here.

admin.site.register(Movie)
admin.site.register(Watched)
admin.site.register(Actor)