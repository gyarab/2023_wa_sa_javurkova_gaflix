from django.contrib import admin
from .models import film

class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')

admin.site.register(film, FilmAdmin)