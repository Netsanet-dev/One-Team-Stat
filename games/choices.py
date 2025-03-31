from django.db import models

class RefereeRole(models.TextChoices):
    MAIN = 'main', 'Main Referee'
    ASSISSTANT_1 = 'assistant 1', 'Assistant Referee 1'
    ASSISSTANT_2 = 'assistant 2', 'Assistant Referee 2'
    FOURTH = 'fourth', 'Fourth Offical'

class GameStatus(models.TextChoices):
    SCHEDULED = 'scheduled', 'Scheduled'
    ONGOING = 'ongoing', 'Ongoing'
    COMPELETED = 'compeleted', 'Compeleted'
    POSTPONED = 'postponed', 'Postponed'
    CANCELED = 'canceled', 'Canceled'

class GameEventType(models.TextChoices):
    DEFAULT = 'default', 'Default' 
    GOAL = 'goal', 'Goal'
    ASSIST = 'assist', 'Assist'
    YELLOW = 'yellow', 'Yellow Card'
    RED = 'red', 'Red card'