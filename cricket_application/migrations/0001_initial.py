# Generated by Django 3.0.5 on 2020-07-25 19:38

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CricketPlayer',
            fields=[
                ('player_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('player_image', models.ImageField(upload_to='players')),
                ('jersey_number', models.IntegerField(unique=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='CricketTeam',
            fields=[
                ('team_id', models.IntegerField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=100)),
                ('team_logo', models.ImageField(upload_to='teams')),
                ('club_state', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('match_id', models.IntegerField(primary_key=True, serialize=False)),
                ('match_type', models.CharField(choices=[('TEST', 'TEST'), ('ODI', 'ODI'), ('T20', 'T20')], max_length=100)),
                ('teamA', models.CharField(max_length=100)),
                ('teamB', models.CharField(max_length=100)),
                ('match_venue', models.CharField(max_length=100)),
                ('match_date', models.DateTimeField()),
                ('match_winner', models.CharField(blank=True, default='--', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matches_played', models.IntegerField(default=0)),
                ('matches_won', models.IntegerField(default=0)),
                ('matches_lost', models.IntegerField(default=0)),
                ('matches_tied', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cricket_application.CricketTeam')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerHistory',
            fields=[
                ('ph_id', models.IntegerField(primary_key=True, serialize=False)),
                ('matches', models.IntegerField()),
                ('runs', models.BigIntegerField()),
                ('highest_score', models.IntegerField()),
                ('fifties', models.IntegerField()),
                ('hundreds', models.IntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricket_application.CricketPlayer')),
            ],
        ),
        migrations.AddField(
            model_name='cricketplayer',
            name='teams',
            field=models.ManyToManyField(to='cricket_application.CricketTeam'),
        ),
    ]
