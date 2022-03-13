from random import choice

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import UserForm, PlayerForm
from .models import Game, Player, Scores
from .utils import who_winner_lottery


def index(request):
    games = Game.objects.filter(
        Q(p1__user=request.user) | Q(p2__user=request.user)
    ).order_by('-date')
    context = {'games': games}
    return render(request, 'games/index.html', context)


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
        gamer, choice_player = who_winner_lottery(gamer, choice_player)
        surface = choice(surfaces)
        game = Game.objects.create(
            p1=gamer,
            p2=choice_player,
            result=choice_score,
            surface=surface
        )
    return redirect('index')


@login_required
@transaction.atomic
def profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        player_form = PlayerForm(request.POST, instance=request.user.player)
        if user_form.is_valid() and player_form.is_valid():
            user_form.save()
            player_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        player_form = PlayerForm(instance=request.user.player)

    return render(request, 'games/player.html', {
        'user_form': user_form,
        'player_form': player_form
    })
