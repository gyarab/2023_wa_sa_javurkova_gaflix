from django.shortcuts import render

from filmy.models import Movie, Director, Actor

def movies(request):
    query = request.GET.get('query')
    if query:
        movies = Movie.objects.filter(name__icontains=query) | Movie.objects.filter(description__icontains=query)
    else:
        movies = Movie.objects.all().order_by('name')
    
    context = {
        'movies': movies,
        'search': True
    }
    return render(request, 'filmy/movies.html', context)


def movie(request, id):
    context = {
        'movie':  Movie.objects.get(id=id)
    }
    return render(request, 'filmy/movie.html', context)


def actors(request):
    query = request.GET.get('query')
    if query:
        actors = Actor.objects.filter(name__icontains=query)
    else:
        actors = Actor.objects.all().order_by('name')
    
    context = {
        'actors': True,
        'people': actors,
        'search': True
    }
    return render(request, 'filmy/people.html', context)


def actor(request, id):
    actor = Actor.objects.get(id=id)
    
    context = {
        'actor': True,
        'person': actor,
        'movies': Movie.objects.filter(actors=actor)
    }
    return render(request, 'filmy/person.html', context)


def directors(request):
    query = request.GET.get('query')
    if query:
        directors = Director.objects.filter(name__icontains=query)
    else:
        directors = Director.objects.all().order_by('name')
    
    context = {
        'people': directors,
        'search': True
    }
    return render(request, 'filmy/people.html', context)


def director(request, id):
    director = Director.objects.get(id=id)
    
    context = {
        'person': director,
        'movies': Movie.objects.filter(director=director)
    }
    return render(request, 'filmy/person.html', context)

