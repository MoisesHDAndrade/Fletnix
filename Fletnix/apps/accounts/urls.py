from django.urls import path
from . import views

app_name = 'user_profile'
urlpatterns = [
    path('register/',views.register, name = 'register'),
    path('login/',views.login, name = 'login'),
    path('detail/', views.profile_detail, name = 'profile_detail'),
    path('update/', views.profile_update, name = 'profile_update')
]