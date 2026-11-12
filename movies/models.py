from django.db import models
from django.contrib.auth.models import User


# Movie Category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Movie Details
class Movie(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='movie_posters/')
    description = models.TextField()
    release_date = models.DateField()
    actors = models.CharField(max_length=500)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trailer_url = models.URLField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Movie Comments
class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# Favourite Movies
class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return self.user.username