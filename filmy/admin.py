from django.contrib import admin
from .models import film

# abych nezapomnela: superuser 'admin' 'unipasswd'

class FilmAdmin(admin.ModelAdmin):
    # list_display = ('title', 'year')
    pass

admin.site.register(film, FilmAdmin)