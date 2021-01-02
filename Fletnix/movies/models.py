from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=255, null=True)
    summary = models.TextField(null=True)
    year = models.CharField(max_length=255, null=True)
    trailer = models.TextField(null=True)
    cast = models.TextField(null=True)
    genre = models.CharField(max_length=255, null=True)
    cover = models.TextField(null=True)
    url = models.TextField(null=True)

    def __str__(self):
        return self.title
