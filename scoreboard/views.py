from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import LibraryForm, GameForm
from .models import Game, User, Wishlist, Library, Catalogue, LibraryCatalogue, WishlistCatalogue
import json

# with open('./video-game.json') as json_file:
#     json_data = json.load(json_file)
#     print(json_data)
# Create your views here.

def homepage(request):
    return render(request, 'scoreboard/homepage.html')

def game_list(request):
    games = Game.objects.all()
    return render(request, 'scoreboard/game_list.html', {'games': games})

def game_detail(request, pk):
    game = Game.objects.get(id=pk)
    return render(request, 'scoreboard/game_details.html', {'game': game})



def wishlist(request):
    catalog = Wishlist.objects.all()
    return render(request, 'scoreboard/wishlist.html', {'catalog': catalog})

# print(Library.game)

def library(request):
    archive = Library.objects.all
    return render(request, 'scoreboard/library.html', {'archive': archive})

def library_add(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            game = form.save()
            return redirect('game_details', pk=game.pk)
    else:
        form = LibraryForm()
    return render(request, 'scoreboard/library_form.html', {'form': form})

def library_delete(request, pk):
    Library.objects.get(id=pk).delete()
    return redirect('game_details')

def game_add(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save()
            return redirect('game_details', pk=game.pk)
    else:
        form = LibraryForm()
    return render(request, 'scoreboard/game_form.html', {'form': form})

def error404(request):
    return render(request, 'scoreboard/404.html')