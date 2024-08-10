from django.contrib import admin
from .models import Game, User, Library, Wishlist, Catalogue, WishlistCatalogue, LibraryCatalogue
# Register your models here.

admin.site.register(Game)
admin.site.register(User)
admin.site.register(Library)
admin.site.register(Wishlist)
admin.site.register(Catalogue)
# admin.site.register(WishlistCatalogue)
# admin.site.register(LibraryCatalogue)