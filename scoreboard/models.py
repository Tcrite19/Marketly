from django.db import models



class Game(models.Model):
    title = models.CharField(max_length=10485)
    description = models.CharField(max_length=10485)
    photo_url = models.CharField(max_length=10485, null=True)

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Wishlist(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='wishlist', default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist', default=1)

class Library(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='library', default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='library', default=1)