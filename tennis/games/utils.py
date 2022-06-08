import csv
from datetime import datetime
from random import choice

from django.contrib.auth.models import User

from .models import Scores, Player


def parsing_tennis_rating_to_db():
    """ Function fill players to base from csv"""
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
    """ Func fill scores to Scores model from csv"""
    with open('../scores_tennis_matches.txt') as sc:
        for s in sc.readlines():
            if not Scores.objects.filter(score=s.rstrip('\n')).exists():
                score = Scores.objects.create(score=s.rstrip('\n'))
                score.save()


def who_winner_lottery(p1, p2):
    """Simple implementation of lottery"""
    if choice((False, True)):
        return p1, p2
    else:
        return p2, p1


if __name__ == '__main__':
    parsing_tennis_rating_to_db()
    # scores()
