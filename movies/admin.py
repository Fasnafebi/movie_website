from django.contrib import admin
from .models import Category, Movie, Comment, Favourite

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(Favourite)