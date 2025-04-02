from django.db import models
from django.contrib.auth.models import AbstractUser

class UserRole(models.TextChoices):
    LEAGUE_ADMIN = 'league','League Admin'
    CLUB_ADMIN = 'club ', 'club Admin'
    TEAM_ADMIN = 'team','Team Admin'
    USER = 'user', 'Regular User'

class MyUser(AbstractUser):
   role = models.CharField(max_length=50, choices=UserRole.choices, default=UserRole.USER)