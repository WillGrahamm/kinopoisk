from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True, blank=True
    )
    # favorit_movies = models.ManyToManyField('kinopoisk.Movie')   