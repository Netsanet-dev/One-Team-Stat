from django.shortcuts import render

from core.models import UserRole
from core.permissions import IsClubAdmin, IsLeagueAdmin, IsRegularUser, IsTeamAdmin

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Fixtures, Lineups, LineupPlayer, Substitution, GameEvents, MatchStats, MatchOfficals
from .serializers import (
    FixtureSerializer,
    LineupSerializer,
    LineupPlayerSerializer,
    SubstitutionSerializer,
    MatchOfficalSerialzer,
    GameEventSerializer,
    MatchStatSerializer
    )

class FixtureViewSet(ModelViewSet):
    queryset = Fixtures.objects.all()
    serializer_class = FixtureSerializer
    

    def get_permissions(self):
        user = self.request.user
        if self.action in ['create','update', 'partial_update', 'destroy']:
            if user.is_authenticated and user.role == UserRole.LEAGUE_ADMIN:
                permission_classes = [IsLeagueAdmin]
            else:
                permission_classes =[]
        if self.action not in ['create', 'update', 'partial_update', 'destroy']:
            if user.is_authenticated and user.role == UserRole.CLUB_ADMIN:
                permission_classes = [IsClubAdmin]
            elif user.is_authenticated and user.role == UserRole.TEAM_ADMIN:
                permission_classes = [IsTeamAdmin]
            elif user.is_authenticated and user.role == UserRole.USER:
                permission_classes = [IsRegularUser]
            else:
                permission_classes = []
        return [permission() for permission in permission_classes]

class LineupViewSet(ModelViewSet):
    queryset = Lineups.objects.all()
    serializer_class = LineupSerializer

    def get_permissions(self):
        user = self.request.user
        if self.action in ['create','update', 'partial_update']:
            if user.is_authenticated and user.role == UserRole.LEAGUE_ADMIN:
                permission_classes = [IsLeagueAdmin]
            elif user.is_authenticated and user.role == UserRole.CLUB_ADMIN:
                permission_classes = [IsClubAdmin]
            elif user.is_authenticated and user.role == UserRole.TEAM_ADMIN:
                permission_classes = [IsTeamAdmin]
            else:
                permission_classes =[]
        elif self.action == 'destroy':
            if user.is_authenticated and user.role == UserRole.LEAGUE_ADMIN:
                permission_classes = [IsLeagueAdmin]
            else:
                permission_classes = []
        if self.action not in ['create', 'update', 'partial_update', 'destroy']:
            if user.is_authenticated and user.role == UserRole.USER:
                permission_classes = [IsRegularUser]
            else:
                permission_classes = []
        return [permission() for permission in permission_classes]

class LineupPlayerViewSet(ModelViewSet):
    queryset = LineupPlayer.objects.all()
    serializer_class = LineupPlayerSerializer

    def get_permissions(self):
        user = self.request.user
        if self.action in ['create','update', 'partial_update']:
            if user.is_authenticated and user.role == UserRole.LEAGUE_ADMIN:
                permission_classes = [IsLeagueAdmin]
            elif user.is_authenticated and user.role == UserRole.CLUB_ADMIN:
                permission_classes = [IsClubAdmin]
            elif user.is_authenticated and user.role == UserRole.TEAM_ADMIN:
                permission_classes = [IsTeamAdmin]
            else:
                permission_classes =[]
        elif self.action == 'destroy':
            if user.is_authenticated and user.role == UserRole.LEAGUE_ADMIN:
                permission_classes = [IsLeagueAdmin]
            else:
                permission_classes = []
        if self.action not in ['create', 'update', 'partial_update', 'destroy']:
            if user.is_authenticated and user.role == UserRole.USER:
                permission_classes = [IsRegularUser]
            else:
                permission_classes = []
        return [permission() for permission in permission_classes]

class SubstitutionViewSet(ModelViewSet):
    queryset = Substitution.objects.all()
    serializer_class = SubstitutionSerializer

    def get_permissions(self):
        user = self.request.user
        if self.action in ['create','update', 'partial_update']:
            if user.is_authenticated and user.role == UserRole.LEAGUE_ADMIN:
                permission_classes = [IsLeagueAdmin]
            elif user.is_authenticated and user.role == UserRole.CLUB_ADMIN:
                permission_classes = [IsClubAdmin]
            elif user.is_authenticated and user.role == UserRole.TEAM_ADMIN:
                permission_classes = [IsTeamAdmin]
            else:
                permission_classes =[]
        elif self.action == 'destroy':
            if user.is_authenticated and user.role == UserRole.LEAGUE_ADMIN:
                permission_classes = [IsLeagueAdmin]
            else:
                permission_classes = []
        if self.action not in ['create', 'update', 'partial_update', 'destroy']:
            if user.is_authenticated and user.role == UserRole.USER:
                permission_classes = [IsRegularUser]
            else:
                permission_classes = []
        return [permission() for permission in permission_classes]

class MatchOfficalViewSet(ModelViewSet):
    queryset = MatchOfficals.objects.all()
    serializer_class = MatchOfficalSerialzer

    def get_permissions(self):
        user = self.request.user
        if self.action in ['create','update', 'partial_update', 'destroy']:
            if user.is_authenticated and user.role == UserRole.LEAGUE_ADMIN:
                permission_classes = [IsLeagueAdmin]
            else:
                permission_classes =[]
        if self.action not in ['create', 'update', 'partial_update', 'destroy']:
            if user.is_authenticated and user.role == UserRole.USER:
                permission_classes = [IsRegularUser]
            elif user.is_authenticated and user.role == UserRole.CLUB_ADMIN:
                permission_classes = [IsClubAdmin]
            elif user.is_authenticated and user.role == UserRole.TEAM_ADMIN:
                permission_classes = [IsTeamAdmin]
            else:
                permission_classes = []
        return [permission() for permission in permission_classes]

class GameEventViewSet(ModelViewSet):
    queryset = GameEvents.objects.all()
    serializer_class = GameEventSerializer

    def get_permissions(self):
        user = self.request.user
        if self.action in ['create','update', 'partial_update', 'destroy']:
            if user.is_authenticated and user.role == UserRole.LEAGUE_ADMIN:
                permission_classes = [IsLeagueAdmin]
            else:
                permission_classes =[]
        if self.action not in ['create', 'update', 'partial_update', 'destroy']:
            if user.is_authenticated and user.role == UserRole.USER:
                permission_classes = [IsRegularUser]
            elif user.is_authenticated and user.role == UserRole.CLUB_ADMIN:
                permission_classes = [IsClubAdmin]
            elif user.is_authenticated and user.role == UserRole.TEAM_ADMIN:
                permission_classes = [IsTeamAdmin]
            else:
                permission_classes = []
        return [permission() for permission in permission_classes]

class MatchStatViewSet(ModelViewSet):
    queryset = MatchStats.objects.all()
    serializer_class = MatchStatSerializer
    
    def get_permissions(self):
        user = self.request.user
        if self.action in ['create','update', 'partial_update', 'destroy']:
            if user.is_authenticated and user.role == UserRole.LEAGUE_ADMIN:
                permission_classes = [IsLeagueAdmin]
            else:
                permission_classes =[]
        if self.action not in ['create', 'update', 'partial_update', 'destroy']:
            if user.is_authenticated and user.role == UserRole.USER:
                permission_classes = [IsRegularUser]
            elif user.is_authenticated and user.role == UserRole.CLUB_ADMIN:
                permission_classes = [IsClubAdmin]
            elif user.is_authenticated and user.role == UserRole.TEAM_ADMIN:
                permission_classes = [IsTeamAdmin]
            else:
                permission_classes = []
        return [permission() for permission in permission_classes]