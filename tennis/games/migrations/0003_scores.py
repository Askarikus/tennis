# Generated by Django 4.0.2 on 2022-02-22 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_remove_player_name_remove_player_surname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(max_length=100)),
            ],
        ),
    ]