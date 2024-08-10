from django import forms
from .models import Game, User, Wishlist, Library, Catalogue

class LibraryForm(forms.ModelForm):

    class Meta:
        model = Catalogue
        fields =('game', 'library', 'wishlist')
