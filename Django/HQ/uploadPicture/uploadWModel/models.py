from django.db import models

class UpForm(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField()
    body = models.TextField()
