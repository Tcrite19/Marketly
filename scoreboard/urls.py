# tunr/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('games/', views.game_list, name='game_list'),
    path('games/<int:pk>', views.game_detail, name='game_details'),
    path('library/', views.library, name='library'),
    path('library/add', views.library_add, name='library_add'),
    path('library/<int:pk>/delete', views.library_delete, name='library_delete'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('games/add', views.game_add, name='game_add'),
    path('*', views.error404, name='error404'),
]