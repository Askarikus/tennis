from random import choice

from django.db.models import Q
from django.shortcuts import render, redirect

from .models import Game, Player, Scores
from .utils import who_winner_lottery


def index(request):
    games = Game.objects.filter(
        Q(p1__user=request.user) | Q(p2__user=request.user)
    ).order_by('-date')
    context = {'games': games}
    return render(request, 'games/index.html', context)


def add_game(request):
    if request.method == 'POST':
        surfaces = (
            'hard',
            'clay',
            'grass',
            'carpet'
        )
        scores = Scores.objects.all()
        choice_score = choice(scores).score
        gamer = request.user.player
        players = Player.objects.exclude(user=request.user)
        choice_player = choice(players)
        gamer, choice_player = who_winner_lottery(gamer, choice_player)
        surface = choice(surfaces)
        game = Game.objects.create(
            p1=gamer,
            p2=choice_player,
            result=choice_score,
            surface=surface
        )
    return redirect('index')
