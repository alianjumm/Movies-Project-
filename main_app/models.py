from django.db import models
from django.urls import reverse 
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

REVIEWS = (
    ('O', 'Okay'),
    ('G', 'Good'),
    ('E', 'Excellent')
)

class Actor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actors_detail', kwargs={'pk': self.id})

class Movie(models.Model):
    title =  models.CharField(max_length=100)
    rating = models.IntegerField()
    description = models.TextField(max_length=2000)
    year = models.IntegerField()
    image = models.URLField(max_length=300, default="http://www.google.com")
    actors = models.ManyToManyField(Actor)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'movie_id': self.id})

    def __str__(self):
        return self.name

class Watched(models.Model):
    date = models.DateField('Watched Date')
    review = models.CharField(max_length=1, choices=REVIEWS, default=REVIEWS[0][0])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_review_display()} on {self.date}"

    class Meta: 
        ordering = ['-date']