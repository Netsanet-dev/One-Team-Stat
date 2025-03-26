import logging
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

MyUser = get_user_model()
logger = logging.getLogger(__name__)

class CookieJWTAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        
        if request.path == "api/token/refresh/":
            return None
        try:
            access_token = request.COOKIES.get(settings.SIMPLE_JWT["AUTH_COOKIE"])
            if access_token:
                try:
                    token = AccessToken(access_token)
                    user_id = token['user_id']
                    user= MyUser.objects.get(id=user_id)
                    request.user = user
                except (InvalidToken, TokenError, MyUser.DoesNotExist) as e:
                    logging.error(f"Token Validation error: {e}")
                    request.user = None
            else:
                request.user = None
        except Exception as e:
            logger.error(f"Middleware error: {e}")
            request.user = None
        return None