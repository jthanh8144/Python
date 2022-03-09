from django.db import models

class contactForm(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.username, self.email