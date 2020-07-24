from django.db import models

# Create your models here.
class User(models.Model):
    location = models.CharField(max_length=100)
    userId = models.TextField()