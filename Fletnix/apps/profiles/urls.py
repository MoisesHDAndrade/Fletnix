from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('add/', views.profile_add, name = 'add'),
    path('edit/<int:pk>/', views.profiles_edit, name = 'edit'),
    path('switchuser/<int:pk>/', views.who_is_watching, name = 'switcher')
]