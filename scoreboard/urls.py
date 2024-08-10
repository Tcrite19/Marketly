# tunr/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('games/', views.game_list, name='game_list'),
    path('games/<int:pk>', views.game_detail, views.library_add,name='game_details'),
    path('library/', views.library, name='library'),
    path('wishlist/', views.wishlist, name='wishlist'),

]