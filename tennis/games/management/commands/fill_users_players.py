import csv
import os
from datetime import datetime
from pathlib import Path

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from games.models import Player

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent



class Command(BaseCommand):
    help = 'Fill to base data for professional players'

    def handle(self, *args, **options):
        with open(os.path.join(BASE_DIR,'player_overviews_unindexed.csv')) as f:
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
                    player = Player.objects.get(user=user)
                    player.birth_date = birth_date
                    player.country = country
                    player.pro = True
                    player.save()