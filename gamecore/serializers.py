from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from datetime import date, timedelta
from .models import (
    League, 
    Stadium, 
    Season,
    Club,
    Team,
    Coach,
    Player, 
    Referee,)

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['id', 'name', 'country', 'gender','divison', 'created_at', 'updated_at']
        validators = [
            UniqueTogetherValidator(
                queryset=League.objects.all(),
                fields=['name', 'country', 'gender','divison'],
                message="Leagues must be unique"
            )
        ]

class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ['id', 'name', 'country', 'city', 'region', 'capacity']


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['id', 'league', 'start', 'end', 'current']

    def validate(self, data):
        start = data.get('start')
        end = data.get('end')
        this_year = date.today().year
        league_days = end- start
        days = timedelta(280)  # 10 month in days

        # 1. In one given year there should be not more than season
        #2. One current season in a league
        #3. The start date must be less than end date.
        if start >= end:
            raise serializers.ValidationError("The 'End date' should be greater than 'Start date'")
        
        #4. Check if the given season is not less than 10 month
        if league_days < days :
            raise serializers.ValidationError("A given season should not be less tha 10 month")
        
        return data


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'stadium', 'name', 'founded_year']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'club', 'league', 'division', 'gender']


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ['id', 'club', 'team', 'first_name', 'last_name', 'gender', 'age', 'nationality', 'position']


class PlayerSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    
    class Meta:
        model = Player
        fields = ['id', 'team', 'first_name', 'last_name', 'gender', 'age', 'nationality', 'dominant_foot', 'positions']

    def validate(self, data):
        team = data.get('id')
        player_gender = data.get('gender')
        
        # Check if Team-gender and Player-Gender are the same.
        if team.gender != player_gender:
            raise serializers.ValidationError(f"Team gender {team.gender} is should be the same with Player Gender {player_gender}")
        return data

class RefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = ['id', 'first_name', 'last_name', 'nationality', 'age', 'gender', 'current_league', 'referee_level']