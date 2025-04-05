import uuid
from gamecore.choices import PlayerPositions
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .choices import GameStatus, GameEventType, RefereeRole
from gamecore.models import Season, League, Team, Referee, Stadium, Player


class Fixtures(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    date_time = models.DateTimeField()
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='fixtures')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='fixtures')
    round = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(40)])
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name='fixtures') 
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_fixtures')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_fixtures')
    home_team_score = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    away_team_score = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    status = models.CharField(max_length=20, choices=GameStatus.choices, default=GameStatus.SCHEDULED)

    def __str__(self):
        return f'Round: {self.round}: {self.home_team.club.name} vs {self.away_team.club.name}'


class Lineups(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    fixture = models.ForeignKey(Fixtures, on_delete=models.CASCADE, related_name='lineups')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='lineups')
    
    def __str__(self):
        return f'Lineup for {self.team} in {self.fixture}'

class LineupPlayer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lineup = models.ForeignKey(Lineups, on_delete=models.CASCADE, related_name='lineups')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='lineups')
    position = models.CharField(max_length=10, choices=PlayerPositions.choices, default=PlayerPositions.GK)
    is_starter = models.BooleanField(default=True)
    is_captain = models.BooleanField(default=False)

    def  __str__(self):
        return {f'{self.player.first_name} {self.player.last_name} {self.is_starter} - {'Starter' if self.starting else 'Substitute'}'}

class Substitution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fixture = models.ForeignKey(Fixtures, on_delete=models.CASCADE, related_name='substitutions')
    player_in = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='sub_in')
    player_out = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='sub_out')
    minute = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(135)])

    def __str__(self):
        return f'Sub: {self.player_in.first_name} -> {self.player_out.first_name} at {self.minute}'


class MatchOfficals(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    fixture =models.ForeignKey(Fixtures, on_delete=models.CASCADE, related_name='match_officals') 
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE, related_name='matches')
    role = models.CharField(max_length=30, choices=RefereeRole.choices, default=RefereeRole.MAIN)

    def __str__(self):
        return f'{self.referee.first_name} - {self.role} in {self.fixture.date_time}'


class GameEvents(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    fixture = models.ForeignKey(Fixtures, on_delete=models.CASCADE, related_name='events')
    minute = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(135)])
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='game_events')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='game_events')
    assist = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_assists', null=True, blank=True)
    event_type = models.CharField(max_length=20, choices=GameEventType.choices, default=GameEventType.DEFAULT)
    value = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.team} - {self.event_type} by {self.player.first_name} {self.player.last_name} at {self.minute}'    


class MatchStats(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fixture = models.ForeignKey(Fixtures, on_delete=models.CASCADE, related_name='team_stats')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teams_stats')
    possession = models.IntegerField(default=50, validators=[MinValueValidator(0), MaxValueValidator(100)])
    total_passes = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    shots = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    shots_on_target = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    shots_off_target = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    fouls = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    corners = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    offsides = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return f'Team: {self.team.club.name if self.team else "N/A"}, Fixture: {self.fixture.date_time if self.fixture else "N/A"} '
    