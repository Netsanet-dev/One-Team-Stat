from django.db import models
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
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
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='images/', blank=True, null=True)
    flag = models.ImageField(upload_to='images/', blank=True, null=True)
    divison = models.CharField(max_length=30, choices=LeagueDivisions.choices, default=LeagueDivisions.TOP)
    gender = models.CharField(max_length=20, choices=Gender.choices, default=Gender.UNSPECIFIED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{"Male" if self.gender == "M" else "Female"} - {self.name} {self.divison} Division "


class Stadium(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    capacity = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(100000)], default=100)

    def __str__(self):
        return f'{self.name}, Capacity: {self.capacity}'


class Season(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='leagues_season')
    start = models.DateField()
    end = models.DateField()
    current = models.BooleanField(default=False)

    def __str__(self):
        return f'{"Current" if self.current else " "} {self.league} From {self.start} to {self.end}'    


class Club(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name='home_teams')
    logo = models.ImageField(upload_to='images/', null=True, blank=True)
    founded_year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(date.today().year)], default=1900,)

    def __str__(self):
        return f"{self.name}"


class Team(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='league_clubs')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='team_clubs')
    division = models.CharField(max_length=50, choices=TeamDivisons.choices, default=TeamDivisons.FIRST)
    gender = models.CharField(max_length=20, choices=Gender.choices, default=Gender.UNSPECIFIED)

    def __str__(self):
        return f'{self.club.name}, {self.division}, {self.gender}' 


class Coach(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='coach_clubs')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='coach_teams')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=Gender.choices, default=Gender.UNSPECIFIED)
    age = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    nationality = models.CharField(max_length=100)
    position = models.CharField(max_length=100, choices=CoachingPositions.choices, default=CoachingPositions.HEAD)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, Coach at {self.club.name}'


class Player(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players_team')
    first_name = models.CharField(max_length=50)
    last_name =models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=Gender.choices, default=Gender.UNSPECIFIED)
    age = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    nationality = models.CharField(max_length=100)
    dominant_foot = models.CharField(max_length=10, choices=DominantFoot.choices, default=DominantFoot.RIGHT)
    positions = models.CharField(max_length=50, choices=PlayerPositions.choices, default=PlayerPositions.GK)

    def __str__(self):
        return f'{self.first_name} {self.last_name} played at {self.team.club.name}'


class Referee(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    gender = models.CharField(max_length=20, choices=Gender.choices, default=Gender.UNSPECIFIED)
    current_league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='referees_league')
    referee_level = models.CharField(max_length=20, choices=RefereeLevel.choices, default=RefereeLevel.OTHER)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'