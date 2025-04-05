from django.urls import path, include
from. import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'league' , views.LeagueVeiwSet, basename='league')
router.register(r'stadium' , views.StadiumVeiwSet, basename='stadium')
router.register(r'season' , views.SeasonVeiwSet, basename='season')
router.register(r'club' , views.ClubVeiwSet, basename='club')
router.register(r'team' , views.TeamVeiwSet, basename='team')
router.register(r'coach' , views.CoachVeiwSet, basename='coach')
router.register(r'player' , views.PlayerViewSet, basename='player')
router.register(r'referee' , views.RefereeViewSet, basename='referee')


urlpatterns =[
    path('', include(router.urls))
]

