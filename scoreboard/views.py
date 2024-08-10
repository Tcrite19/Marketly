from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import LibraryForm, WishlistForm
from .models import Game, User, Wishlist, Library
import json

with open('./video-game.json') as json_file:
    json_data = json.load(json_file)
    print(json_data)
# Create your views here.

def homepage(request):
    return render(request, 'scoreboard/homepage.html')

def game_list(request):
    games = Game.objects.all()
    return render(request, 'scoreboard/game_list.html', {'games': games})

# def game_detail(request, pk):
#     game = Game.objects.get(id=pk)
#     return render(request, 'scoreboard/game_detail.html', {'games': game})

def library(request):
    catalog = Library.objects.all()
    return render(request, 'scoreboard/library.html', {'catalog': catalog})

def wishlist(request):
    catalog = Wishlist.objects.all()
    return render(request, 'scoreboard/wishlist.html', {'catalog': catalog})

# print(Library.game)

def library_add(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            library = form.save()
            return redirect('library')
    else:
        form = LibraryForm()
    return render(request, "scoreboard/library.html")