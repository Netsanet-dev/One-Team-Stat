from django.urls import path, include
from. import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'league' , views.LeagueVeiwSet)
router.register(r'stadium' , views.StadiumVeiwSet)
router.register(r'season' , views.SeasonVeiwSet)
router.register(r'club' , views.ClubVeiwSet)
router.register(r'team' , views.TeamVeiwSet)
router.register(r'coach' , views.CoachVeiwSet)
router.register(r'player' , views.PlayerViewSet)
router.register(r'referee' , views.RefereeViewSet)


urlpatterns = [
    path('', include(router.urls))
]

