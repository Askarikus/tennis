from datetime import datetime
import csv
from random import choice

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Q
from django.utils.timezone import now

from .models import Game, Player, Scores


def parsing_tennis_rating():
    """ Fuction fill players to base"""
    with open('../player_overviews_unindexed.csv') as f:
        f.readline()
        spamreader = csv.reader(f, delimiter=',', quotechar='"')
        for s in spamreader:
            username = s[1]
            if not User.objects.filter(username=username).exists():
                first_name = s[2]
                last_name = s[3]
                user = User.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name
                )
                user.save()
                birth_date = None
                country = ''
                if s[8]:
                    birth_date = datetime.strptime(s[8], '%Y.%m.%d')
                if s[7]:
                    country = s[7].split(',')[-1]
                player = Player.objects.create(
                    user=user,
                    birth_date=birth_date,
                    country=country
                )
                player.save()
    pass


def scores_to_db():
    with open('../scores.csv') as sc:
        for s in sc.readlines():
            if not Scores.objects.filter(score=s.rstrip('\n')).exists():
                score = Scores.objects.create(score=s.rstrip('\n'))
                score.save()


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
            result_game=choice_score,
            surface=surface
        )
        game.save()
    return redirect('index')
