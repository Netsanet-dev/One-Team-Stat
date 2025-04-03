from django.conf import settings

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import get_authorization_header
from rest_framework_simplejwt.exceptions import TokenError



class CustomCookieJWTAuthentication(JWTAuthentication):
    """Custom JWT authentication class that uses cookies for access and refresh tokens."""
    # Modify authenticate class
    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        
        if not auth or auth[0].lower() == b'bearer':
            return super().authenticate(request)
            
        access_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE'])
        refresh_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_REFRESH_COOKIE'])
    
        if not access_token:
            return None
            
        try:
            validated_token = self.get_validated_token(access_token)
            return self.get_user(validated_token), validated_token
        
        except TokenError:
            if not refresh_token:
                return None