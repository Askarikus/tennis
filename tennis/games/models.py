from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #name = models.CharField(max_length=50)
    #surname = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Game(models.Model):
    p1 = models.ForeignKey(to=Player, on_delete=models.PROTECT,
                           related_name='p1')
    p2 = models.ForeignKey(to=Player, on_delete=models.PROTECT,
                           related_name='p2')
    date_game = models.DateTimeField(auto_now_add=True)
    result_game = models.CharField(max_length=50)
    surface = models.CharField(max_length=6)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.p1.user.first_name} {self.p1.user.last_name} - ' \
               f'{self.p2.user.first_name} {self.p2.user.last_name} ' \
               f'{self.result_game} f{self.surface}'

    class Meta:
        ordering: ['-date_game']


class Scores(models.Model):
    score = models.CharField(max_length=100)

    def __str__(self):
        return self.score


