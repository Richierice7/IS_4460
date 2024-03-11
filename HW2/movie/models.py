from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField(max_length=11, null=False)
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=500, null=True)
    director = models.CharField(max_length=100, null=True)
    release_year = models.CharField(max_length=50, null=True)
    budget = models.CharField(max_length=50, null=True)
    runtime = models.CharField(max_length=50, null=True)
    rating = models.CharField(max_length=50, null=True)
    genre = models.CharField(max_length=50, null=True)

class User(models.Model):
    user_id = models.IntegerField(max_length=11, null=False)
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True, null=True)

# Write Django QuerySet statements for Movie:
    
# Retrieve all movies:
# movies = Movie.objects.all()
    
# Filter for movies starting with some text
# filter = Movie.objects.exclude(title__startswith=("T"))
    
# Get one movie
# movie = Movie.objects.get(title="Bolt")
    
# Update one movie
# movie_six.title = "Cars"
# movie_six.save()
    
# Delete one movie
# movie_eight.delete()
