from django.shortcuts import render

from .models import Game


def index(request):
    games = Game.objects.filter(p1__user=request.user)
    context = {'games': games}

    return render(request, 'games/index.html', context)
