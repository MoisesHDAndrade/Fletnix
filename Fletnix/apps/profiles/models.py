from django.db import models
from Fletnix.apps.accounts.models import UserProfile

class Profiles(models.Model):
    ADULT  = '1'
    CHILD = '2'
    USER_RATE_CHOICE = [
        (ADULT, 'Adult'),
        (CHILD, 'Child')
    ]


    MALE = '1'
    FEMALE = '2'
    USER_GENDER_CHOICE =[
        (MALE, 'Male'),
        (FEMALE, 'Female')
        ]
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='profiles')
    user_name = models.CharField(max_length=255, null=True)
    user_age = models.CharField(max_length=1, choices=USER_RATE_CHOICE, default=ADULT)
    user_gender = models.CharField(max_length=1, choices=USER_GENDER_CHOICE, default=MALE)

    def __str__(self):
        return self.user_name
