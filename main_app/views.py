from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import Movie, Actor
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.forms import WatchedForm
from .forms import WatchedForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

# class Movie:
#     def __init__(self, title, rating, description, year):
#         self.title = title
#         self.rating = rating
#         self.description = description
#         self.year = year

# movies = [
#     Movie('Avengers: Infinity War', '8.5 IMDb', 'Iron Man, Thor, the Hulk and the rest of the Avengers unite to battle their most powerful enemy yet -- the evil Thanos. On a mission to collect all six Infinity Stones, Thanos plans to use the artifacts to inflict his twisted will on reality. The fate of the planet and existence itself has never been more uncertain as everything the Avengers have fought for has led up to this moment.', 2018),
#     Movie('Rush Hour', '7 IMDb', 'When a Chinese diplomat s daughter is kidnapped in Los Angeles, he calls in Hong Kong Detective Inspector Lee (Jackie Chan) to assist the FBI with the case. But the FBI doesn t want anything to do with Lee, and they dump him off on the LAPD, who assign wisecracking Detective James Carter (Chris Tucker) to watch over him. Although Lee and Carter cant stand each other, they choose to work together to solve the case on their own when they figure out they ve been ditched by both the FBI and police.', 1998),
#     Movie('Inception', '8.8 IMDb', 'Dom Cobb (Leonardo DiCaprio) is a thief with the rare ability to enter people s dreams and steal their secrets from their subconscious. His skill has made him a hot commodity in the world of corporate espionage but has also cost him everything he loves. Cobb gets a chance at redemption when he is offered a seemingly impossible task: Plant an idea in someone s mind. If he succeeds, it will be the perfect crime, but a dangerous enemy anticipates Cobb s every move.', 2010)
# ]

class MovieCreate(LoginRequiredMixin, CreateView):
    model= Movie
    fields = ['title', 'rating', 'description', 'year', 'image']
    # success_url = '/movies/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = '__all__'
 
class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    success_url = '/movies/'

class ActorList(LoginRequiredMixin, ListView):
    model = Actor
 
class ActorDetail(LoginRequiredMixin, DetailView):
    model = Actor
 
class ActorCreate(LoginRequiredMixin, CreateView):
    model = Actor
    fields = '__all__'
 
class ActorUpdate(LoginRequiredMixin, UpdateView):
    model = Actor
    fields = ['name']
 
class ActorDelete(LoginRequiredMixin, DeleteView):
    model = Actor
    success_url = '/actors/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def movies_index(request):
    movies = Movie.objects.filter(user = request.user)
    return render(request, 'movies/index.html', {'movies': movies})

@login_required
def movies_details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)

    actors_movie_doesnt_have = Actor.objects.exclude(id__in = movie.actors.all().values_list('id'))

    watched_form = WatchedForm()
    return render(request, 'movies/detail.html', {'movie': movie, 'watched_form': watched_form, 'actors': actors_movie_doesnt_have})

@login_required
def add_watched(request, movie_id):
    form = WatchedForm(request.POST)
    if form.is_valid():
        new_watched = form.save(commit=False)
        new_watched.movie_id = movie_id
        new_watched.save()
    return redirect('detail', movie_id = movie_id)

@login_required
def assoc_actor(request, movie_id, actor_id):
    Movie.objects.get(id=movie_id).actors.add(actor_id)
    return redirect('detail', movie_id=movie_id)

@login_required
def unassoc_actor(request, movie_id, actor_id):
    Movie.objects.get(id=movie_id).actors.remove(actor_id)
    return redirect('detail', movie_id=movie_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = "Invalid Signup - Try Again"
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

