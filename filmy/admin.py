from django.contrib import admin
from .models import Movie, Actor, Director, Genre

class MovieAdmin(admin.ModelAdmin):
    # genres je ManyToManyField, museli jsme definovat vlastni diplay funkci v models.py
    list_display = ['id', 'name', 'year', 'genres_display', 'footage', 'director']
    # ze zobrazovanych atributu udelam links, muzu na ne klikat
    list_display_links = ['id', 'name']
    # search bar
    # '=field' -> hleda se exact match
    search_fields = ['=id', 'name', 'director__name']
    # filtrovani
    list_filter = ['year', 'genres']
    # to co je v 'list_display_links' se neda dat sem
    list_editable = ['year', 'footage', 'director']


class ActorAdmin(admin.ModelAdmin):
    pass


class DirectorAdmin(admin.ModelAdmin):
    pass


class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Genre, GenreAdmin)