# Generated by Django 4.0.2 on 2022-02-19 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=100)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=30)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_game', models.DateTimeField(default=django.utils.timezone.now)),
                ('result_game', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('p1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='p1', to='games.player')),
                ('p2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='p2', to='games.player')),
            ],
        ),
    ]
