from datetime import datetime
import csv

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

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
    games = Game.objects.filter(p1__user=request.user)
    context = {'games': games}
    scores_to_db()
    #parsing_tennis_rating()
    return render(request, 'games/index.html', context)


def add_game(request):
    if request.method == 'POST':
        print('post')

    return redirect('index')
