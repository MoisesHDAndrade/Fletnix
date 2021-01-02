from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('index/', views.movie_index, name = 'index'),
    path('', views.movie_searcher, name = 'searcher'),
    path('movie/<int:pk>/', views.movie_info, name = 'info'),
    path('new/',views.movie_add, name = 'add')
]