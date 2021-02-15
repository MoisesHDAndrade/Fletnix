from django.db import models
from django.db.models.deletion import DO_NOTHING
from Fletnix.apps.accounts.models import UserProfile

class Profiles(models.Model):

    AVATAR1 = 'avatar1'
    AVATAR2 = 'avatar2'
    AVATAR3 = 'avatar3'
    AVATAR4 = 'avatar4'
    AVATAR5 = 'avatar5'
    AVATAR6 = 'avatar6'
    AVATAR7 = 'avatar7'
    AVATAR8 = 'avatar8'
    AVATAR9 = 'avatar9'

    USER_AVATAR_CHOICE = [
        (AVATAR1, 'avatar1'),
        (AVATAR2, 'avatar2'),
        (AVATAR3, 'avatar3'),
        (AVATAR4, 'avatar4'),
        (AVATAR5, 'avatar5'),
        (AVATAR6, 'avatar6'),
        (AVATAR7, 'avatar7'),
        (AVATAR8, 'avatar8'),
        (AVATAR9, 'avatar9'),
    ]


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
    user_avatar = models.CharField(max_length=20, choices=USER_AVATAR_CHOICE, default=AVATAR1, null=True)

    def __str__(self):
        return self.user_name


class WhoIsWatching(models.Model):
    person = models.ForeignKey(Profiles, on_delete=models.CASCADE, related_name='profile_watching')
    person_avatar = models.CharField(max_length=50, null=True)
    person_age = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.person)