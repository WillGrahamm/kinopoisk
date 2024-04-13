from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('', movies_list, name='movies_list'),
    path('movie_detail/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('', actors_list, name='actors_list'),
    path('actor_detail/<int:actor_id>/', actor_detail, name='actor_detail'),
    path('', directors_list, name='directors_list'),
    path('director_detail/<int:director_id>/', director_detail, name='director_detail'),
    path('', sound_engineers_list, name='sound_engineers_list'),
    path('sound_engineer_detail/<int:se_id>/', sound_engineer_detail, name='sound_engineer_detail'),
    path('', genres_list, name='genres_list'),
    path('genre_detail/<int:genre_id>/', genre_detail, name='genre_detail'),
]
