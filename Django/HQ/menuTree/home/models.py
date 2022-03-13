from django.db import models

class catagory(models.Model):
    name = models.CharField(max_length=25)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s <--%s" %(self.parent, self.name)