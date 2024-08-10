from django import forms
from .models import Game, User, Wishlist, Library

class LibraryForm(forms.ModelForm):

    class Meta:
        model = Library
        fields =('game', 'user')

class WishlistForm(forms.ModelForm):

    class Meta:
        model = Wishlist
        fields =('game', 'user')