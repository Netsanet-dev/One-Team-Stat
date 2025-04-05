from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'fixtures', views.FixtureViewSet)
router.register(r'lineups', views.LineupViewSet)
router.register(r'lineup_players', views.LineupPlayerViewSet)
router.register(r'susbstitution', views.SubstitutionViewSet)
router.register(r'match_officals', views.MatchOfficalViewSet)
router.register(r'game_events', views.GameEventViewSet)
router.register(r'match_stats', views.MatchStatViewSet)



urlpatterns =[
    path('', include(router.urls))
]
