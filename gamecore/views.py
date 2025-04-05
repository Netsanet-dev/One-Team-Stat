from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from .models import Referee, League, Stadium, Season, Club, Team, Coach, Player
from core.permissions import IsLeagueAdmin, IsClubAdmin, IsRegularUser, IsTeamAdmin
from core.models import UserRole
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


class LeagueVeiwSet(viewsets.ModelViewSet):
    serializer_class = LeagueSerializer
   
    def get_queryset(self):
        queryset = League.objects.all()
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        gender = self.request.query_params.get('gender', None)
        
        # filter by id
        if id:
            queryset = queryset.filter(id=id)
        # filter by name
        if name:
            queryset = queryset.filter(name=name)
        
        # filter by gender
        if gender:
            queryset = queryset.filter(gender=gender)

        return queryset
    
    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create','update', 'partial_update', 'destroy']:
            permission_classes = [IsLeagueAdmin]
        return [permission() for permission in permission_classes]

class StadiumVeiwSet(viewsets.ModelViewSet):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create','update', 'partial_update', 'destroy']:
            permission_classes = [IsLeagueAdmin]
        return [permission() for permission in permission_classes]

class SeasonVeiwSet(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create','update', 'partial_update', 'destroy']:
            permission_classes = [IsLeagueAdmin]
        return [permission() for permission in permission_classes]


class ClubVeiwSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create','update', 'partial_update']:
            permission_classes = [IsClubAdmin|IsLeagueAdmin]
        elif self.action == 'destroy':
            permission_classes = [IsLeagueAdmin]
        print(permission_classes)
        return [permission() for permission in permission_classes]
    
class TeamVeiwSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_fields = ['name']

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create','update', 'partial_update', 'destroy']:
            permission_classes = [IsLeagueAdmin]
        return [permission() for permission in permission_classes]

class CoachVeiwSet(viewsets.ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create','update', 'partial_update', 'destroy']:
            permission_classes = [IsLeagueAdmin]
        return [permission() for permission in permission_classes]


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create','update', 'partial_update', 'destroy']:
            permission_classes = [IsLeagueAdmin]
        return [permission() for permission in permission_classes]


class RefereeViewSet(viewsets.ModelViewSet):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer
    

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create','update', 'partial_update', 'destroy']:
            permission_classes = [IsLeagueAdmin]
        return [permission() for permission in permission_classes]

