from django.db import models
from django.contrib.auth.models import AbstractUser

USER_ROLE_ADMIN = 'admin'
USER_ROLE_PLAYER = 'player'
USER_ROLE_COACH = 'coach'
USER_ROLE_USER = 'user'

ROLE_CHOICES = (
        (USER_ROLE_ADMIN, 'Administrator'),
        (USER_ROLE_PLAYER, 'Player'),
        (USER_ROLE_COACH, 'Coach'),
        (USER_ROLE_USER, 'Regular User')
    )

class MyUser(AbstractUser):
   role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='user')