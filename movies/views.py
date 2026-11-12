from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Movie, Category
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm, CommentForm
def movie_list(request):
    movies = Movie.objects.all()
    categories = Category.objects.all()

    search_query = request.GET.get('search')

    if search_query:
        movies = movies.filter(title__icontains=search_query)

    return render(request, 'movies/movie_list.html', {
        'movies': movies,
        'categories': categories,
        'search_query': search_query
    })

@login_required
def add_movie(request):

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)

        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user
            movie.save()

            messages.success(request, 'Movie added successfully!')
            return redirect('movie_list')

    else:
        form = MovieForm()

    return render(request, 'movies/add_movie.html', {'form': form})
@login_required
def edit_movie(request, movie_id):

    movie = get_object_or_404(
        Movie,
        id=movie_id,
        added_by=request.user
    )

    if request.method == 'POST':
        form = MovieForm(
            request.POST,
            request.FILES,
            instance=movie
        )

        if form.is_valid():
            form.save()
            messages.success(request, 'Movie updated successfully!')
            return redirect('movie_list')

    else:
        form = MovieForm(instance=movie)

    return render(request, 'movies/edit_movie.html', {
        'form': form
    })
@login_required
def delete_movie(request, movie_id):

    movie = get_object_or_404(
        Movie,
        id=movie_id,
        added_by=request.user
    )

    if request.method == 'POST':
        movie.delete()
        messages.success(request, 'Movie deleted successfully!')

    return redirect('movie_list')
def movies_by_category(request, category_id):

    category = get_object_or_404(Category, id=category_id)

    movies = Movie.objects.filter(category=category)

    return render(request, 'movies/category_movies.html', {
        'category': category,
        'movies': movies
    })
@login_required
def add_comment(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()

            messages.success(request, 'Comment added successfully!')

    return redirect('movie_list')