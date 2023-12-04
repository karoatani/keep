from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    title = models.CharField(max_length=500)
    content = models.TextField()
