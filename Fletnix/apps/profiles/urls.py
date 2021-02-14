from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('add', views.profile_add, name = 'add')
]