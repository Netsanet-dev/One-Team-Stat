from django.contrib import admin
from .models import League, Season, Club, Player, Coach, Team, Stadium, Referee

# Register your models here.
@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ['league_id', 'name', 'country', 'divison', 'created_at', 'updated_at']

@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country', 'city', 'region', 'capacity']

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['league_id', 'start', 'end', 'current']

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['club_id', 'league_id', 'name', 'founded_year']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_id', 'club_id', 'division', 'gender']


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ['coach_id', 'club_id', 'team_id', 'first_name', 'last_name', 'gender', 'age', 'nationality', 'position']


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['player_id', 'team_id', 'first_name', 'last_name', 'gender', 'age', 'nationality', 'dominant_foot', 'positions']


@admin.register(Referee)
class RefereeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'nationality', 'age', 'gender', 'current_league', 'referee_level']
