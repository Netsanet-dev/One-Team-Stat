from rest_framework import serializers
from gamecore.models import Player, Team
from gamecore.serializers import PlayerSerializer
from .models import Fixtures, Lineups, Substitution, MatchOfficals, GameEvents, MatchStats, LineupPlayer


class FixtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixtures
        fields = ['id', 'date_time', 'league', 'season', 'round', 'stadium', 
                  'home_team', 'away_team', 'home_team_score', 'away_team_score', 'status']

class LineupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lineups
        fields = ['id', 'fixture', 'team']

class LineupPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineupPlayer
        fields = ['id', 'lineup', 'player', 'position', 'is_starter', 'is_captain']
    

class SubstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Substitution
        fields = ['id', 'fixture', 'player_in', 'player_out', 'minute']

    def validate(self, data):
        player_in = data.get('player_in')
        player_out = data.get('player_out')

        # Assign team id to a player
        p_in = player_in.team.id
        o_out = player_out.team.id

        # Check if a player change already exists
        player_change = Substitution.objects.filter(player_in=player_in, player_out=player_out).exists()
       
       #1. If a player already changed, cannot be changed.
        if player_change:
            raise serializers.ValidationError("Already Player Changed!")
        
        #2. A player cannot change himself
        if player_in == player_out:
            raise serializers.ValidationError("A player cannot change himself.")
        
        #3. A player cannot change another team player
        if p_in != o_out:
            raise serializers.ValidationError("A player cannot change another team player")
        
        #4 .A player after changed cannot played again in that game.
        return data

class MatchOfficalSerialzer(serializers.ModelSerializer):
    class Meta:
        model = MatchOfficals
        fields = ['id', 'fixture', 'referee', 'role']


class GameEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameEvents
        fields = ['id', 'fixture', 'minute', 'team', 'player', 'assist', 'event_type', 'value']

class MatchStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchStats
        fields = ['id', 'fixture', 'team', 'possession', 'total_passes', 'shots', 
                  'shots_on_target', 'shots_off_target', 'fouls', 'corners', 'offsides']