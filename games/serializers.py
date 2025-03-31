from rest_framework import serializers
from gamecore.models import Player, Team
from .models import Fixtures, Lineups, Substitution, MatchOfficals, GameEvents, MatchStats


class FixtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixtures
        fields = ['id', 'date_time', 'league', 'season', 'round', 'stadium', 'home_team', 'away_team', 'home_team_score', 'away_team_score', 'status']

class LineupSerializer(serializers.ModelSerializer):
    player_data= serializers.SerializerMethodField()
    player = serializers.PrimaryKeyRelatedField(queryset=Player.objects.none())
    
    class Meta:
        model = Lineups
        fields = ['id', 'fixture','player','player_data', 'starting', 'sub', 'captain']

    #1 . Check if a player is not assigned more than  once
    def get_player_data(self, obj):
        home_team = obj.fixture.home_team
        away_team = obj.fixture.away_team
        players = Player.objects.filter(team__in=[home_team, away_team])
        print(away_team)
        return [{'player_id':player.player_id, 'name': player.first_name} for player in players]
    
    def validate(self, data):
        fixture = data.get('fixture')
        player = data.get('player')
        starting = data.get('starting')
        captain = data.get('captain')
        sub = data.get('sub')
        if fixture and player:
            home_team = fixture.home_team
            away_team = fixture.away_team

            if player.team  not in [home_team, away_team]:
                raise serializers.ValidationError({'Player Error':"Player is not in the home or away team"})
            
            if Lineups.objects.filter(fixture=fixture, player=player):
                raise serializers.ValidationError({"Lineup Error": "A played already in the starting"})
            
            if captain and Lineups.objects.filter(fixture=fixture, captain=True).exists():
                raise serializers.ValidationError({'Captain Error': 'Captain already assigned.'})
            
            if starting and sub:
                raise serializers.ValidationError({'Startin and Sub Error': 'A player cannot be in both startin and Substitution.'})
        return data
    
    def get_fields(self):
        fields = super().get_fields()
        fixture_id = self.context.get('fixture_id')
        if fixture_id:
            try:
                fixture = Fixtures.objects.get(id=fixture_id)
                home_team = fixture.home_team
                away_team = fixture.away_team
                fields['player'].queryset = Player.objects.filter(team__in=[home_team, away_team])
            except Fixtures.DoesNotExist:
                pass
        return fields
    #2. Check if a one team player is not assigned to other team
    #3. 


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
        fields = ['id', 'fixture', 'team', 'possession', 'total_passes', 'shots', 'shots_on_target', 'shots_off_target', 'fouls', 'corners', 'offsides']