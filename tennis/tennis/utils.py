import csv
from datetime import datetime
# from django.contrib.auth.models import User

# from tennis.games.models import Player


# def parsing_tennis_rating():
#     """ Function fill players to base"""
#     with open('../player_overviews_unindexed.csv') as f:
#         f.readline()
#         spamreader = csv.reader(f, delimiter=',', quotechar='"')
#         for s in spamreader:
#             username = s[1]
#             if not User.objects.filter(username=username).exists():
#                 first_name = s[2]
#                 last_name = s[3]
#                 user = User.objects.create(
#                     username=username,
#                     first_name=first_name,
#                     last_name=last_name
#                 )
#                 user.save()
#                 birth_date = None
#                 country = ''
#                 if s[8]:
#                     birth_date = datetime.strptime(s[8], '%Y.%m.%d')
#                 if s[7]:
#                     country = s[7].split(',')[-1]
#                 player = Player.objects.create(
#                     user=user,
#                     birth_date=birth_date,
#                     country=country
#                 )
#                 player.save()
#     pass
from random import choice


def scores():
    with open('../scores_tennis_matches.txt', 'r') as f,\
                 open('../scores.csv', 'w') as scores_m:
        set_of_scores = set(f.readlines())
        for elem in set_of_scores:
            print(elem.rstrip('\n'), file=scores_m)



if __name__ == '__main__':
    # parsing_tennis_rating()
    scores()
