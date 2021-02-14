from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ENGLISH = '?language=en-US'
    PORTUGUES = '?language=pt-BR'
    USER_LANGUAGE_CHOICE = [
        (ENGLISH, 'English'),
        (PORTUGUES, 'Portugues')
    ]

    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    user_language = models.CharField(max_length=30, choices=USER_LANGUAGE_CHOICE, default=ENGLISH)
    

    def __str__(self):
        return str(self.user)
