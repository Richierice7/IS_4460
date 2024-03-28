from django.urls import path
from . import views
from .views import MovieListCreateView, MovieDetailView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-details'),
    path('list/', views.MovieList.as_view(), name='movie-list'),
    path('movie_add/<int:movie_id>/', views.MovieAdd.as_view(), name='movie-add'),
    path('movie_add/', views.MovieAdd.as_view(), name='movie-add'),
    path('movie_update/<int:movie_id>/', views.MovieUpdate.as_view(), name='movie-update'),
    path('movie_update/', views.MovieUpdate.as_view(), name='movie-update'),
    path('movie_delete/<int:movie_id>/', views.MovieDelete.as_view(), name='movie-delete'),
]