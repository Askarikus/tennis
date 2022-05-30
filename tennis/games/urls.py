from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('add_game', views.add_game, name='add_game'),
    path('profile', views.profile, name='profile'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('delete_game/<int:id>', views.delete_game, name='delete_game'),
    path('add_user', views.add_user, name='add_user'),
]
