from django.shortcuts import render
from .models import *

def main(request):
    movies = Movie.objects.all()
    return render(request, 'kinopoisk/main.html', {'movies' : movies})

def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'kinopoisk/movies_list.html', {'movies' : movies})

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id = movie_id)
    return render(request, 'kinopoisk/movie_detail.html', {'movie' : movie})

def actors_list(request):
    actors = MoviePerson.objects.filter(role = MoviePerson.RoleType.ACTOR)
    return render(request, 'kinopoisk/actors_list.html', {
        'persons': actors, 'title': 'Актеры'
    })

def actor_detail(request, actor_id):
    actor = Movie.objects.get(id = actor_id)
    movies = actor.acted_in_movies.all()
    return render(request, 'kinopoisk/actor_detail.html', {
        'person': actor, 'movies': movies
    })

def directors_list(request):
    directors = MoviePerson.objects.filter(role = MoviePerson.RoleType.DIRECTORS)
    return render(request, 'kinopoisk/directors_list.html', {
        'persons': directors, 'title': 'Режиссеры'
    })

def director_detail(request, director_id):
    director = Movie.objects.get(id = director_id)
    movies = director.acted_in_movies.all()
    return render(request, 'kinopoisk/director_detail.html', {
        'person': director, 'movies': movies
    })

def sound_engineers_list(request):
    sound_engineers = MoviePerson.objects.filter(role = MoviePerson.RoleType.SOUND_ENGINEERS)
    return render(request, 'kinopoisk/sound_engineers_list.html', {
        'persons': sound_engineers, 'title': 'Звукорежиссеры'
    })

def sound_engineer_detail(request, se_id):
    sound_engineer = MoviePerson.objects.get(id = se_id)
    movies = sound_engineer.acted_in_movies.all()
    return render(request, 'kinopoisk/main.html', {
        'person': sound_engineer, 'movies': movies
    })

def genres_list(request):
    genres = Movie.objects.all()
    return render(request, 'kinopoisk/genres_list.html', {'genres': genres})

def genre_detail(request, genre_id):
    genre = Movie.objects.get(id = genre_id)
    movies = Movie.objects.all()
    return render(request, 'kinopoisk/genre_detail.html', {
        'genre': genre, 'movies': movies
    })

