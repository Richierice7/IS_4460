from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .models import Movie
from .forms import MovieForm
from rest_framework import generics
from .serializers import MovieSerializer

# Create your views here.
class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieList(View):

    def get(self,request):

        movies = Movie.objects.all()

        return render(request = request,template_name = 'movie/movie-list.html',context = {'movies':movies})
    
class MovieAdd(View):

    def get(self,request,movie_id=None):

        if movie_id:
            movie = Movie.objects.get(pk=movie_id)
        else:
            movie = Movie()

        form = MovieForm(instance=movie)

        return render(request = request,
                      template_name = 'movie/movie-add.html',
                      context = {'movie':movie,'form':form})
    
    def post(self,request,movie_id=None):

        if movie_id:
            movie = Movie.objects.get(pk=movie_id)
        else:
            movie = Movie()

        form = MovieForm(request.POST,instance=movie)

        if form.is_valid():
            order = form.save()

            return redirect(reverse("movie-list"))
        
        return render(request = request,template_name = 'movie/movie_add.html',context = {'movie':movie,'form':form})

class MovieUpdate(View):

    def get(self,request,movie_id=None):

        if movie_id:
            movie = Movie.objects.get(pk=movie_id)
        else:
            movie = Movie()

        form = MovieForm(instance=movie)

        return render(request = request,
                      template_name = 'movie/movie-update.html',
                      context = {'movie':movie,'form':form})
    
    def post(self,request,movie_id=None):

        if movie_id:
            movie = Movie.objects.get(pk=movie_id)
        else:
            movie = Movie()

        form = MovieForm(request.POST,instance=movie)

        if form.is_valid():
            order = form.save()

            return redirect(reverse("movie-list"))
        
        return render(request = request,template_name = 'movie/movie_update.html',context = {'movie':movie,'form':form})

class MovieDelete(View):


    def get(self,request,movie_id=None):

        if movie_id:
            movie = Movie.objects.get(pk=movie_id)
        else:
            movie = Movie()

      


        form = MovieForm(instance=movie)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'customer_app/movie-delete.html',context = {'order':movie,'form':form})
      
    
    def post(self,request,movie_id=None):

        movie = Movie.objects.get(pk=movie_id)

        form = MovieForm(request.POST,instance=movie)

        movie.delete()

        return redirect(reverse("movie-list"))
    
