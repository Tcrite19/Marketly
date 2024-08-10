# tunr/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('games/', views.game_list, name='game_list'),
    # path('games/<int:pk>', views.game_detail, name='game_detail'),
    path('library/', views.library, name='library'),
    path('wishlist/', views.wishlist, name='wishlist'),

]