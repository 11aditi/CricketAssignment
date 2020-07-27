from django.db import models
from django_countries.fields import CountryField


class CricketTeam(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=100)
    team_logo = models.ImageField(upload_to='teams')
    club_state = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name


class CricketPlayer(models.Model):
    player_id = models.IntegerField(primary_key=True)
    teams = models.ManyToManyField(CricketTeam)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    player_image = models.ImageField(upload_to='players')
    jersey_number = models.IntegerField(unique=True)
    country = CountryField(multiple=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class PlayerHistory(models.Model):
    ph_id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(CricketPlayer, on_delete=models.CASCADE)
    matches = models.IntegerField()
    runs = models.BigIntegerField()
    highest_score = models.IntegerField()
    fifties = models.IntegerField()
    hundreds = models.IntegerField()

    def __str__(self):
        return self.player.first_name


MATCH_TYPE_CHOICES = (('TEST', 'TEST'), ('ODI', 'ODI'), ('T20', 'T20'))


class Matches(models.Model):
    match_id = models.IntegerField(primary_key=True)
    match_type = models.CharField(choices=MATCH_TYPE_CHOICES, max_length=100)
    teamA = models.CharField(max_length=100)
    teamB = models.CharField(max_length=100)
    match_venue = models.CharField(max_length=100)
    match_date = models.DateTimeField()
    match_winner = models.CharField(default='--', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.match_venue


class Points(models.Model):
    team = models.OneToOneField(CricketTeam, on_delete=models.CASCADE)
    matches_played = models.IntegerField(default=0)
    matches_won = models.IntegerField(default=0)
    matches_lost = models.IntegerField(default=0)
    matches_tied = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.team.team_name
