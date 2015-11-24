from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname  = models.CharField(max_length=20)
    email     = models.CharField(max_length=100)
    password  = models.CharField(max_length=32)

