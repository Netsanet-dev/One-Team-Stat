import logging
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

logger = logging.getLogger(__name__)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Custom claims
        try:
            token['name'] = user.username
            token['email'] = user.email
            token['role'] = user.role
        except AttributeError:            
            logger.error("Token claim have got error.")
            pass
        return token