from urllib import request
from django.db import models

class postModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    body = models.TextField()

    def __Str__(self):
        return self.title

