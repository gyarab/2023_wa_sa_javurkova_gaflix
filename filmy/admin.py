from django.contrib import admin
from .models import Movie, Actor, Director, Genre

class MovieAdmin(admin.ModelAdmin):
    pass


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