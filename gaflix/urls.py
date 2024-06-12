from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from filmy.views import movies, movie, director, directors, actor, actors

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="filmy/index.html")),
    path('druhy/', TemplateView.as_view(template_name="filmy/druhy.html")),
    path('filmy/', movies, name='movies'),
    path('film/<int:id>/', movie, name='movie'),
    path('reziseri/', directors, name='directors'),
    path('reziser/<int:id>/', director, name='director'),
    path('herci/', actors, name='actors'),
    path('herec/<int:id>/', actor, name='actor')
]
