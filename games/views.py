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
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create','update', 'partial_update', 'destroy']:
            permission_classes = [IsLeagueAdmin]
        return [permission() for permission in permission_classes]

class LineupViewSet(ModelViewSet):
    queryset = Lineups.objects.all()
    serializer_class = LineupSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create','update', 'partial_update', 'destroy']:
            permission_classes = [IsLeagueAdmin]
        return [permission() for permission in permission_classes]

class LineupPlayerViewSet(ModelViewSet):
    queryset = LineupPlayer.objects.all()
    serializer_class = LineupPlayerSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create','update', 'partial_update', 'destroy']:
            permission_classes = [IsLeagueAdmin]
        return [permission() for permission in permission_classes]

class SubstitutionViewSet(ModelViewSet):
    queryset = Substitution.objects.all()
    serializer_class = SubstitutionSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create','update', 'partial_update', 'destroy']:
            permission_classes = [IsLeagueAdmin]
        return [permission() for permission in permission_classes]

class MatchOfficalViewSet(ModelViewSet):
    queryset = MatchOfficals.objects.all()
    serializer_class = MatchOfficalSerialzer

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create','update', 'partial_update', 'destroy']:
            permission_classes = [IsLeagueAdmin]
        return [permission() for permission in permission_classes]

class GameEventViewSet(ModelViewSet):
    queryset = GameEvents.objects.all()
    serializer_class = GameEventSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create','update', 'partial_update', 'destroy']:
            permission_classes = [IsLeagueAdmin]
        return [permission() for permission in permission_classes]

class MatchStatViewSet(ModelViewSet):
    queryset = MatchStats.objects.all()
    serializer_class = MatchStatSerializer
    
    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create','update', 'partial_update', 'destroy']:
            permission_classes = [IsLeagueAdmin]
        return [permission() for permission in permission_classes]