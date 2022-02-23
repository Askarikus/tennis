# Generated by Django 4.0.2 on 2022-02-23 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_scores'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='surface',
            field=models.CharField(default='hard', max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='date_game',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
