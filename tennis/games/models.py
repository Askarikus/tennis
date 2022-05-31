from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    pro = models.BooleanField(default=False)  # is Player profi or not

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Player.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.player.save()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'



class Game(models.Model):
    p1 = models.ForeignKey(to=Player, on_delete=models.PROTECT,
                           related_name='p1')
    p2 = models.ForeignKey(to=Player, on_delete=models.PROTECT,
                           related_name='p2')
    date = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=50)
    surface = models.CharField(max_length=6)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.p1.user.first_name} {self.p1.user.last_name} - ' \
               f'{self.p2.user.first_name} {self.p2.user.last_name} ' \
               f'{self.result_game} f{self.surface}'

    class Meta:
        ordering: ['-date_game']


class Scores(models.Model):
    """ Storage of all variants games result. This Implemented for random
    choose and pasting to games"""
    score = models.CharField(max_length=100)

    def __str__(self):
        return self.score
