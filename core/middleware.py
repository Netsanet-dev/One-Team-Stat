import logging


from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

MyUser = get_user_model()
logger = logging.getLogger(__name__)

class CookieJWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def process_request(self, request):
        if request.path == "/api/token/refresh/":
            return None

        access_token_key = settings.SIMPLE_JWT.get("AUTH_COOKIE", "access_token")
        refresh_token_key = "refresh_token"

        access_token = request.COOKIES.get(access_token_key)
        refresh_token = request.COOKIES.get(refresh_token_key)

        if not access_token:
            request.user = None
            return None

        try:
            token = AccessToken(access_token)
            user_id = token["user_id"]
            request.user = MyUser.objects.get(id=user_id)
        except (InvalidToken, TokenError):
            logger.warning(f"Invalid token for user {user_id}.")
            request.user = None

    def process_response(self, request, response):
        access_token_key = settings.SIMPLE_JWT.get("AUTH_COOKIE", "access_token")
        refresh_token_key = "refresh_token"

        refresh_token = request.COOKIES.get(refresh_token_key)

        if request.user is None and refresh_token:
            try:
                new_refresh = RefreshToken(refresh_token)
                new_access_token = str(new_refresh.access_token)

                response.set_cookie(
                    access_token_key, 
                    new_access_token,
                    httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'], 
                    secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
                    path=settings.SIMPLE_JWT['AUTH_COOKIE_PATH'],
                )
            except TokenError:
                logger.warning("Invalid refresh token, user must log in again.")

        return response

    def __call__(self, request):
        response = self.get_response(request)
        return response