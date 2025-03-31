from django.contrib import admin
from .models import League, Season, Club, Player, Coach, Team, Stadium, Referee

# Register your models here.
@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country', 'divison','gender', 'created_at', 'updated_at']

@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country', 'city', 'region', 'capacity']

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['id', 'league', 'start', 'end', 'current']

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'founded_year']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'club', 'league' ,'division', 'gender']


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ['id', 'club', 'team', 'first_name', 'last_name', 'gender', 'age', 'nationality', 'position']


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'team', 'first_name', 'last_name', 'gender', 'age', 'nationality', 'dominant_foot', 'positions']


@admin.register(Referee)
class RefereeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'nationality', 'age', 'gender', 'current_league', 'referee_level']
