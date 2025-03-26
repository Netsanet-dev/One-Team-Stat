from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import get_authorization_header


class CustomCookieJWTAuthentication(JWTAuthentication):
    
    # Modify authenticate class
    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != b'bearer':
            try:
                token = request.COOKIES.get("access_token")
                if token is None:
                    return None
            except KeyError:
                return None
            validated_token = self.get_validated_token(token)
            return self.get_user(validated_token), validated_token
        else:
            return super().authenticate(request)