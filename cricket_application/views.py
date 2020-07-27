from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.shortcuts import render
from django.contrib import messages
from .models import *


def homeview(request):
    team_list = CricketTeam.objects.all()
    no_of_teams = len(team_list)
    player_list = CricketPlayer.objects.all()
    no_of_players = len(player_list)
    matches = Matches.objects.all()
    no_of_matches = len(matches)
    matches_not_com = Matches.objects.filter(match_winner='--').count()
    matches_com = no_of_matches - matches_not_com
    context = {
        'teams': team_list,
        'teams_count': no_of_teams,
        'players': player_list,
        'players_count': no_of_players,
        'matches': matches,
        'matches_count': no_of_matches,
        'match_com': matches_com,
        'match_ncom': matches_not_com,
    }
    return render(request, 'home.html', context)


def TeamList(request):
    teams = CricketTeam.objects.all()
    context = {'teams': teams}
    return render(request, 'team_list.html', context)


def TeamDetailView(request, team_id):
    team = CricketTeam.objects.get(pk=team_id)
    context = {'team': team}
    return render(request, 'team_detail.html', context)


class PlayerDetailView(DetailView):
    model = PlayerHistory
    object = PlayerHistory.objects.all()
    template_name = 'player_profile.html'


team_list = []


def CreateMatch(request):
    teams = CricketTeam.objects.all()
    for team in teams:
        team_list.append(team.team_name)

    team_names = list(set(team_list))
    context = {'teamlist': team_names}
    return render(request, 'matchform.html', context)


def save_match(request):
    match_id = request.POST['match_id']
    match_type = request.POST['match_type']
    teamA_name = request.POST.get('TeamA')
    teamB_name = request.POST.get('TeamB')
    match_venue = request.POST['match_venue']
    match_date = request.POST['match_date']
    if teamA_name == teamB_name:
        messages.warning(request, 'TeamA and TeamB should not be same')
        return redirect('cricket_application:matches_create')
    else:
        data = Matches(match_id=match_id, match_type=match_type, teamA=teamA_name, teamB=teamB_name,
                       match_venue=match_venue, match_date=match_date)
        data.save()
        messages.success(request, 'match created successfully')
        return redirect('cricket_application:MatchFixtures')


def MatchView(request):
    matches = Matches.objects.all()
    return render(request, 'match_fixture.html', {'matches': matches})


def TeamPoints(request):
    points = Points.objects.all()
    return render(request, 'points.html', {'points': points})
