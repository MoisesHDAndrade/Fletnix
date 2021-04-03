from django.db import models
from django.contrib.auth.models import User
import requests
from django.conf import settings
from django.core.files import File
import os
import urllib
from urllib.parse import urlparse
from urllib import request as req
from tempfile import NamedTemporaryFile
import pathlib
from io import StringIO

import imghdr # Used to validate images

# Used to imitate reading from byte file
from PIL import Image # Holds downloaded image and verifies it
import copy # Copies instances of Image

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

    
   



    
    def __str__(self):
        return self.title
