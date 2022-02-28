from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Game, Player


@admin.register(Player)
class GamesAdmin(ModelAdmin):
    pass


@admin.register(Game)
class GamesAdmin(ModelAdmin):
    list_per_page = 20
    pass
