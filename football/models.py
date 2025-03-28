import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from .choices import (
    Gender,
    DominantFoot,
    PlayerPositions,
    CoachingPositions,
    LeagueDivisions,
    TeamDivisons,
    RefereeLevel
)

class League(models.Model):
    league_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='images/', blank=True, null=True)
    flag = models.ImageField(upload_to='images/', blank=True, null=True)
    divison = models.CharField(max_length=30, choices=LeagueDivisions.choices, default=LeagueDivisions.TOP)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"League name: {self.name} Country: {self.country}"


class Stadium(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    capacity = models.PositiveBigIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Season(models.Model):
    league_id = models.ForeignKey(League, on_delete=models.SET_NULL, null=True,related_name='leagues_season')
    start = models.DateField()
    end = models.DateField()
    current = models.BooleanField(default=False)

    def __str__(self):
        return f'League: {self.league_id.name} Start: {self.start}'


class Club(models.Model):
    club_id = models.BigAutoField(primary_key=True)
    league_id = models.ForeignKey(League, on_delete=models.SET_NULL, related_name='league_clubs', null=True)
    name = models.CharField(max_length=200)
    stadium = models.ForeignKey(Stadium, on_delete=models.SET_NULL, null=True, blank=True, related_name='home_teams')
    logo = models.ImageField(upload_to='images/', null=True, blank=True)
    founded_year = models.PositiveBigIntegerField()

    def __str__(self):
        return f"Club name: {self.name}"


class Team(models.Model):
    team_id = models.BigAutoField(primary_key=True, editable=False)
    club_id = models.ForeignKey(Club, on_delete=models.SET_NULL, related_name='team_clubs', null=True)
    division = models.CharField(max_length=50, choices=TeamDivisons.choices, default=TeamDivisons.FIRST)
    gender = models.CharField(max_length=10, choices=Gender.choices, default="")

    def __str__(self):
        return f'{self.club_id.name}, {self.division}, {self.gender}' 


class Coach(models.Model):
    coach_id = models.BigAutoField(primary_key=True, editable=False)
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='coach_clubs')
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='coach_teams')
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=Gender.choices, default="")
    age = models.IntegerField()
    nationality = models.CharField(max_length=100)
    position = models.CharField(max_length=100, choices=CoachingPositions.choices, default=CoachingPositions.HEAD)

    def __str__(self):
        return f'Coach: {self.first_name} {self.last_name}'


class Player(models.Model):
    player_id = models.BigAutoField(primary_key=True, editable=False)
    team_id = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='players_team')
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name =models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=Gender.choices, default="")
    age = models.IntegerField(default=1)
    nationality = models.CharField(max_length=100)
    dominant_foot = models.CharField(max_length=10, choices=DominantFoot.choices, default=DominantFoot.RIGHT)
    positions = models.CharField(max_length=50, choices=PlayerPositions.choices, default=PlayerPositions.GK)

    def __str__(self):
        return f'{self.player_id}, Player: {self.first_name} {self.last_name}'


class Referee(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=Gender.choices, default="")
    current_league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True, related_name='referees_league')
    referee_level = models.CharField(max_length=20, choices=RefereeLevel.choices, default=RefereeLevel.OTHER)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class PlayerStat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='players_stat')
    date = models.DateField(default=timezone.now().date())
    appearances = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)

    def __str__(self):
        return f'Player_ID: {self.player}, Player Name: {self.player.first_name} {self.player.last_name}'




