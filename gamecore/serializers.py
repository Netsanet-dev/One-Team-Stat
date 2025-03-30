from rest_framework import serializers
from .models import (
    League, 
    Stadium, 
    Season,
    Club,
    Team,
    Coach,
    Player, 
    Referee)

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['league_id', 'name', 'country', 'divison', 'created_at', 'updated_at']


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ['id', 'name', 'country', 'city', 'region', 'capacity']


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['id', 'league_id', 'start', 'end', 'current']


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['club_id', 'league_id', 'stadium', 'name', 'founded_year']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['team_id', 'club_id', 'division', 'gender']


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ['coach_id', 'club_id', 'team_id', 'first_name', 'last_name', 'gender', 'age', 'nationality', 'position']


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['player_id', 'team_id', 'first_name', 'last_name', 'gender', 'age', 'nationality', 'dominant_foot', 'positions']


class RefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = ['id', 'first_name', 'last_name', 'nationality', 'age', 'gender', 'current_league', 'referee_level']
        depth = 1

