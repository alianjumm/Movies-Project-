from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class Movie:
    def __init__(self, title, rating, description, year):
        self.title = title
        self.rating = rating
        self.description = description
        self.year = year

movies = [
    Movie('Avengers: Infinity War', '8.5 IMDb', 'Iron Man, Thor, the Hulk and the rest of the Avengers unite to battle their most powerful enemy yet -- the evil Thanos. On a mission to collect all six Infinity Stones, Thanos plans to use the artifacts to inflict his twisted will on reality. The fate of the planet and existence itself has never been more uncertain as everything the Avengers have fought for has led up to this moment.', 2018),
    Movie('Rush Hour', '7 IMDb', 'When a Chinese diplomat s daughter is kidnapped in Los Angeles, he calls in Hong Kong Detective Inspector Lee (Jackie Chan) to assist the FBI with the case. But the FBI doesn t want anything to do with Lee, and they dump him off on the LAPD, who assign wisecracking Detective James Carter (Chris Tucker) to watch over him. Although Lee and Carter cant stand each other, they choose to work together to solve the case on their own when they figure out they ve been ditched by both the FBI and police.', 1998),
    Movie('Inception', '8.8 IMDb', 'Dom Cobb (Leonardo DiCaprio) is a thief with the rare ability to enter people s dreams and steal their secrets from their subconscious. His skill has made him a hot commodity in the world of corporate espionage but has also cost him everything he loves. Cobb gets a chance at redemption when he is offered a seemingly impossible task: Plant an idea in someone s mind. If he succeeds, it will be the perfect crime, but a dangerous enemy anticipates Cobb s every move.', 2010)
]


def home(request):
    return HttpResponse('<h1> Movies Collector </h1>')

def about(request):
    return render(request, 'about.html')

def movies_index(request):
    return render(request, 'movies/index.html', {'movies': movies})