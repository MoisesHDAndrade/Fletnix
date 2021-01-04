from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=255, null=True, default='')
    summary = models.TextField(null=True,default='')
    year = models.CharField(max_length=255, null=True,default='')
    trailer = models.TextField(null=True,default='')
    cast = models.TextField(null=True,default='')
    genre = models.CharField(max_length=255, null=True,default='')
    cover = models.TextField(null=True,default='')
    url = models.TextField(null=True,default='')

    def __str__(self):
        return self.title
