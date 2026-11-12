from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileForm


def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, 'Welcome! Your registration was successful.')
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('movie_list')

        messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')
@login_required
def profile(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')

    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'accounts/profile.html', {'form': form})