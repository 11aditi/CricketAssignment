from django.contrib import admin

from . models import *

class Team(admin.ModelAdmin):
    list_display = ['team_id','team_name','team_logo','club_state']

admin.site.register(CricketTeam,Team)
admin.site.register(CricketPlayer)
admin.site.register(PlayerHistory)
admin.site.register(Matches)
admin.site.register(Points)
