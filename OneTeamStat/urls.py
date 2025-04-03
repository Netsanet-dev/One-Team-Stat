from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from debug_toolbar.toolbar import debug_toolbar_urls

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Collect all my api urls to one place
class APIRootView(APIView):
    def get(self, request, format=None):
        return Response(
            {
                # Core app urls
                "core": {
                # This is for resolving the uri issoue
                "register": request.build_absolute_uri("api/core/register/"),
                "login": request.build_absolute_uri("api/core/login/"),
                "logout": request.build_absolute_uri("api/core/logout/"),
                "update_info": request.build_absolute_uri("api/core/update_info/"),
                "update_password": request.build_absolute_uri("api/core/update_password/"),
                "protected": request.build_absolute_uri("api/core/protected/"),
            },
                # Gamecore app urls
                "gamecore": request.build_absolute_uri("api/gamecore/"),
                # Games app urls
                "games": request.build_absolute_uri("api/games/"),
            }
        )


urlpatterns = [
    path('admin/', admin.site.urls),
  
    # My app urls
    path('', APIRootView.as_view(), name="root-view"), 
    path('api/core/', include('core.urls')),
    path('api/games/', include('games.urls')),
    path('api/gamecore/', include('gamecore.urls')),
  
    # SimpleJWT Path for token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + debug_toolbar_urls()

# This is for serving static files in developement
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)