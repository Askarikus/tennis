import csv
from datetime import datetime

from django.contrib.auth.models import User

from tennis.games.models import Scores, Player


def parsing_tennis_rating_to_db():
    """ Function fill players to base"""
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
                    country=country,
                    pro=True
                )
                player.save()


def parsing_scores_to_db():
    with open('../scores.csv') as sc:
        for s in sc.readlines():
            if not Scores.objects.filter(score=s.rstrip('\n')).exists():
                score = Scores.objects.create(score=s.rstrip('\n'))
                score.save()
