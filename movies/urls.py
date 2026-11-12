from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('add/', views.add_movie, name='add_movie'),
    path('edit/<int:movie_id>/', views.edit_movie, name='edit_movie'),
    path('delete/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    path('category/<int:category_id>/', views.movies_by_category, name='movies_by_category'),
    path('comment/<int:movie_id>/',views.add_comment, name='add_comment'),
    
]   