from django.db import models
from django.contrib.auth.models import User


class Movies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, default='')
    summary = models.TextField(null=True,default='')
    year = models.CharField(max_length=255, null=True,default='')
    trailer = models.TextField(null=True,default='')
    cast = models.TextField(null=True,default='')
    genre = models.CharField(max_length=255, null=True,default='')
    cover = models.TextField(null=True,default='')
    url = models.TextField(null=True,default='')
    image = models.ImageField(upload_to = 'images/', null=True, blank = True)
    relevance = models.CharField(max_length=10, null=True, blank=True)
    certification = models.CharField(max_length=10, null=True, blank=True)

    
    def __str__(self):
        return self.title
