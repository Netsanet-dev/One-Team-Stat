from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Fixtures, Season, Lineups, Substitution, GameEvents, MatchStats, MatchOfficals
from .serializers import (
    FixtureSerializer,
    LineupSerializer,
    SubstitutionSerializer,
    MatchOfficalSerialzer,
    GameEventSerializer,
    MatchStatSerializer
    )

class FixtureViewSet(ModelViewSet):
    queryset = Fixtures.objects.all()
    serializer_class = FixtureSerializer

class LineupViewSet(ModelViewSet):
    queryset = Lineups.objects.all()
    serializer_class = LineupSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        fixture_id = self.request.query_params.get('fixture_id')
        if fixture_id:
            context['fixture_id']= fixture_id
        return context

class SubstitutionViewSet(ModelViewSet):
    queryset = Substitution.objects.all()
    serializer_class = SubstitutionSerializer

class MatchOfficalViewSet(ModelViewSet):
    queryset = MatchOfficals.objects.all()
    serializer_class = MatchOfficalSerialzer

class GameEventViewSet(ModelViewSet):
    queryset = GameEvents.objects.all()
    serializer_class = GameEventSerializer

class MatchStatViewSet(ModelViewSet):
    queryset = MatchStats.objects.all()
    serializer_class = MatchStatSerializer