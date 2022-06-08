import os
from pathlib import Path

from django.core.management.base import BaseCommand

from games.models import Scores

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

class Command(BaseCommand):
    help = 'Fill to base data all possible scores'

    def handle(self, *args, **options):
        """ Func fill scores to Scores model from csv"""
        with open(os.path.join(BASE_DIR,'scores_tennis_matches.txt')) as sc:
            for s in sc.readlines():
                if not Scores.objects.filter(score=s.rstrip('\n')).exists():
                    score = Scores.objects.create(score=s.rstrip('\n'))
                    score.save()
