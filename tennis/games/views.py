from random import choice

from django.db.models import Q
from django.shortcuts import render, redirect

from .models import Game, Player, Scores


def index(request):
    games = Game.objects.filter(
        Q(p1__user=request.user) | Q(p2__user=request.user)
    ).order_by('-date_game')
    context = {'games': games}
    # scores_to_db()
    # parsing_tennis_rating()
    return render(request, 'games/index.html', context)


def who_winner(p1, p2):
    """Simple implementation of lottery"""
    if choice((False, True)):
        return p1, p2
    else:
        return p2, p1


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
        gamer, choice_player = who_winner(gamer, choice_player)
        surface = choice(surfaces)
        game = Game.objects.create(
            p1=gamer,
            p2=choice_player,
            result=choice_score,
            surface=surface
        )

    return redirect('index')
