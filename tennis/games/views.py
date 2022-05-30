from random import choice

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .forms import UserForm, PlayerForm
from .models import Game, Player, Scores
from .utils import who_winner_lottery

class index_class(ListView):
    model = Game
    template_name = 'games/index.html'
    paginator_class = Paginator
    paginate_by = 10
    def get(self, request, *args, **kwargs):
        games = Game.objects.filter(
            Q(p1__user=request.user) | Q(p2__user=request.user)
        ).order_by('-date')
        paginator = Paginator(games, 10)
        page_number = request.GET.get("page")
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            # If page is not an integer, show first page.
            page = paginator.page(1)
        except EmptyPage:
            # If page is out of range, show last existing page.
            page = paginator.page(paginator.num_pages)

        context = {
            'games': games,
            # "object_list": page
        }
        return render(request, self.template_name, context)

def index(request):
    if not request.user.pk:
        return redirect('login')
    games = Game.objects.filter(
        Q(p1__user=request.user) | Q(p2__user=request.user)
    ).order_by('-date')
    paginator = Paginator(games, 24)
    page_number = request.GET.get("page")
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, show first page.
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range, show last existing page.
        page = paginator.page(paginator.num_pages)

    context = {
        'games': games,
        "object_list": page
    }
    return render(request, 'games/index.html', context)


def login(request):
    return render(request, 'account/login.html')


def logout(request):
    return render(request, 'account/logout.html')


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


def delete_game(request, id):
    game = Game.objects.get(pk=id)
    game.delete()
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

def add_user(request):
    print('Hello from add_user')
    # if request.method == 'POST':
    #     if not User.objects.filter(username=username).exists():
    #         first_name = s[2]
    #         last_name = s[3]
    #         user = User.objects.create(
    #             username=username,
    #             first_name=first_name,
    #             last_name=last_name
    #         )
    #         user.save()
    #         birth_date = None
    #         country = ''
    #         if s[8]:
    #             birth_date = datetime.strptime(s[8], '%Y.%m.%d')
    #         if s[7]:
    #             country = s[7].split(',')[-1]
    #         player = Player.objects.create(
    #             user=user,
    #             birth_date=birth_date,
    #             country=country,
    #             pro=True
    #         )
    #         player.save()
    return render(request, 'account/signup.html')
