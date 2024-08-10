from django import forms
from .models import Game, User, Wishlist, Library, Catalogue

class LibraryForm(forms.ModelForm):

    class Meta:
        model = Catalogue
        fields =('game', 'library', 'wishlist')

class GameForm(forms.ModelForm):


    class Meta:
        model = Game
        fields = ('title', 'description', 'photo_url')
