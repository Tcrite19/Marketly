from django.db import models

# Create your models here.
class Developers(models.Model):
    name = models.CharField(max_length=100)

class Games(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    developers = models.ForeignKey(Developers, on_delete=models.CASCADE, related_name='games')

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Wishlist(models.Model):
    games = models.ForeignKey(Games, on_delete=models.CASCADE, related_name='wishlist')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')

class Library(models.Model):
    games = models.ForeignKey(Games, on_delete=models.CASCADE, related_name='library')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='library')