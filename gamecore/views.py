from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated
from .models import League, Stadium, Season, Club, Team, Coach, Player, Referee
from .serializers import (
    LeagueSerializer,
    StadiumSerializer,
    SeasonSerializer,
    ClubSerializer,
    TeamSerializer,
    CoachSerializer,
    PlayerSerializer,
    RefereeSerializer
)

# Create your views here.
class LeagueVeiwSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    permission_classes = [IsAuthenticated]


class StadiumVeiwSet(viewsets.ModelViewSet):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [IsAuthenticated]


class SeasonVeiwSet(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    permission_classes = [IsAuthenticated]


class ClubVeiwSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [IsAuthenticated]

class TeamVeiwSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]


class CoachVeiwSet(viewsets.ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    permission_classes = [IsAuthenticated]


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]


class RefereeViewSet(viewsets.ModelViewSet):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer
    permission_classes = [IsAuthenticated]


