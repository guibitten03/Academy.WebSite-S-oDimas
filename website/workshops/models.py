from django.db import models

# Create your models here.
class Workshops(models.Model):
    name = models.CharField(max_length=200)
    hour = models.CharField(max_length=200)
    room = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name