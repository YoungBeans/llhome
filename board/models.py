from django.db import models

# Create your models here.

class Board(models.Model) :
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    content = models.TextField()
    password = models.CharField(max_length=20)
    User_info = models.ForeignKey('User_info', models.CASCADE)

class User_info(models.Model) :
    user_id = models.CharField(max_length=20)
    password = models.CharField(max_length=20)