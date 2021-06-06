from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.MovieIndexView.as_view(), name = 'index'),
    path('library/movie/', views.MovieSearchView.as_view(), name = 'library_search'),
    path('searcher/', views.movie_searcher, name = 'searcher'),
    path('movie/info/<int:pk>/', views.movie_info, name = 'info'),
    path('new/',views.movie_add, name = 'add'),
    path('library/movie/<int:pk>/', views.movie_detail, name = 'detail'),

    path('save_title/',views.save_titles),

    path('api/movies/', views.MoviesAddApiView.as_view(), name='list_api_view'),
    path('api/movies/<int:pk>/', views.MovieUpdateApiView.as_view(), name='movie_update_view'),
   
    
]