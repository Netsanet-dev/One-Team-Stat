from django.contrib import admin
from .models import Fixtures, Lineups, LineupPlayer, Substitution, MatchOfficals, GameEvents, MatchStats

# Register your models here.
@admin.register(Fixtures)
class FixtureAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_time', 'league', 'season', 'round', 'stadium',
                     'home_team', 'away_team', 'home_team_score', 'away_team_score', 'status']

@admin.register(Lineups)
class LineupAdmin(admin.ModelAdmin):
    list_display = ['id', 'fixture', 'team']

@admin.register(LineupPlayer)
class LineupPlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'lineup', 'player', 'position', 'is_starter', 'is_captain']

@admin.register(Substitution)
class SubstitutionAdmin(admin.ModelAdmin):
    list_display = ['id', 'fixture', 'player_in', 'player_out', 'minute']

@admin.register(MatchOfficals)
class MatchOfficalAdmin(admin.ModelAdmin):
    list_display = ['id', 'fixture', 'referee', 'role']

@admin.register(GameEvents)
class GameEventAdmin(admin.ModelAdmin):
    list_display = ['id', 'fixture', 'minute', 'team', 'player', 'assist', 'event_type', 'value']

@admin.register(MatchStats)
class MatchStatAdmin(admin.ModelAdmin):
    list_display = ['id', 'fixture', 'team', 'possession', 'total_passes',
                     'shots', 'shots_on_target', 'shots_off_target', 'fouls', 'corners', 'offsides']