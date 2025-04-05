from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

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

class StadiumVeiwSet(viewsets.ModelViewSet):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer

    def get_permissions(self):
        user = self.request.user
        if self.action in ['create','update', 'partial_update', 'destroy']:
            if user.is_authenticated and user.role == UserRole.LEAGUE_ADMIN:
                permission_classes = [IsLeagueAdmin]
            elif user.is_authenticated and user.role == UserRole.CLUB_ADMIN:
                permission_classes = [IsClubAdmin]
            else:
                permission_classes =[]
        else:
            permission_classes = [IsRegularUser]
        return [permission() for permission in permission_classes]

class SeasonVeiwSet(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

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
            elif user.is_authenticated and user.role ==  UserRole.USER:
                permission_classes = [IsRegularUser]
            else:
                permission_classes = []
        return [permission() for permission in permission_classes]


class ClubVeiwSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

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
            elif user.is_authenticated and user.role == UserRole.CLUB_ADMIN:
                permission_classes = [IsClubAdmin]
            else:
                permission_classes =[]
        if self.action not in ['create', 'update', 'partial_update', 'destroy']:
            if user.is_authenticated and user.role ==  UserRole.USER:
                permission_classes = [IsRegularUser]
            else:
                permission_classes = []
        return [permission() for permission in permission_classes]

class TeamVeiwSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_fields = ['name']

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
            elif user.is_authenticated and user.role == UserRole.CLUB_ADMIN:
                permission_classes = [IsClubAdmin]
            else:
                permission_classes =[]
        if self.action not in ['create', 'update', 'partial_update', 'destroy']:
            if user.is_authenticated and UserRole.role == UserRole.USER:
                permission_classes = [IsRegularUser]
            else:
                permission_classes = []
        return [permission() for permission in permission_classes]

class CoachVeiwSet(viewsets.ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

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
            elif user.is_authenticated and user.role == UserRole.CLUB_ADMIN:
                permission_classes = [IsClubAdmin]
            else:
                permission_classes =[]
        if self.action not in ['create', 'update', 'partial_update', 'destroy']:
            if user.is_authenticated and user.role ==  UserRole.USER:
                permission_classes = [IsRegularUser]
            else:
                permission_classes = []
        return [permission() for permission in permission_classes]


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

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
            elif user.is_authenticated and user.role == UserRole.CLUB_ADMIN:
                permission_classes = [IsClubAdmin]
            else:
                permission_classes =[]
        if self.action not in ['create', 'update', 'partial_update', 'destroy']:
            if user.is_authenticated and user.role ==  UserRole.USER:
                permission_classes = [IsRegularUser]
            else:
                permission_classes = []
        return [permission() for permission in permission_classes]


class RefereeViewSet(viewsets.ModelViewSet):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer
    

    def get_permissions(self):
        user = self.request.user
        if self.action in ['create','update', 'partial_update', 'destroy']:
            if user.is_authenticated and user.role == UserRole.LEAGUE_ADMIN:
                permission_classes = [IsLeagueAdmin]
            else:
                permission_classes =[]
        if self.action not in ['create', 'update', 'partial_update', 'destroy']:
            if user.is_authenticated and user.role ==  UserRole.USER:
                permission_classes = [IsRegularUser]
            elif user.is_authenticated and user.role == UserRole.CLUB_ADMIN:
                permission_classes = [IsClubAdmin]
            elif user.is_authenticated and user.role == UserRole.TEAM_ADMIN:
                permission_classes = [IsTeamAdmin]
            else:
                permission_classes = []
        return [permission() for permission in permission_classes]


