from django.urls import path

from . import views

app_name = 'cricket_application'

urlpatterns = [
    path('', views.homeview, name='home'),
    path('teams/', views.TeamList, name='team_list'),
    path('teams/<team_id>/', views.TeamDetailView, name='team_detail'),
    path('player_detail/<pk>/', views.PlayerDetailView.as_view(), name='player_detail'),
    path('matches/', views.CreateMatch, name='matches_create'),
    path('save_match/', views.save_match, name='save_match'),
    path('MatchFixtures/', views.MatchView, name='MatchFixtures'),
    path('points_table/', views.TeamPoints, name='teamPoints'),
]
