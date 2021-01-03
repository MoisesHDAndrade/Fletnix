from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_index, name = 'index'),
    path('searcher/', views.movie_searcher, name = 'searcher'),
    path('movie/info/<int:pk>/', views.movie_info, name = 'info'),
    path('new/',views.movie_add, name = 'add'),
    path('movie/library/<int:pk>/', views.movie_detail, name = 'detail')  
]