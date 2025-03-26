# from rest_framework.parsers import JSONParser
import logging
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .serializers import (
    UserRegistrationSerializer,
    UserProfileUpdate, 
    UpdatePasswordSerialzier
)

# Get the Custom User Model
MyUser = get_user_model()
logger = logging.getLogger(__name__)


@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'User': serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({'Message' : "Invalid Username or Password"})

    user = authenticate(request, username=username, password=password)
    
    if user:
        try:
            refresh = RefreshToken.for_user(user)

            response = Response({"Message" : "Login Successful."}, status=status.HTTP_200_OK)
            
            response.set_cookie(
                key=settings.SIMPLE_JWT["access_token"], 
                value=str(refresh.access_token), 
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
                path=settings.SIMPLE_JWT['AUTH_COOKIE_PATH'] )
            
            response.set_cookie(
                key=settings.SIMPLE_JWT["refresh_token"], 
                value=str(refresh), 
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
                path=settings.SIMPLE_JWT['AUTH_COOKIE_PATH'],
            )    
            return response
        
        except Exception as e:
            logger.error(f"Error during login: {e}")
            return Response({"Message": "Internal Server Error."})
    return Response({'Message': "Incorrect Username or Password"},status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()

        response = Response({'message': 'Logout Successful'}, status=status.HTTP_200_OK)
        
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        
        return response

    except Exception as e:
        logger.error(f"Logout error: {e}")
        return Response({'refresh token': f"{refresh_token}"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    user = request.user
    if user:
        return Response({"Message": f"{user.username} Congratulations You are seeing this."})
    return Response({"Message": "Unauthorized"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_info(request):
    user = request.user
    serializer = UserProfileUpdate(user, data=request.data, partial=True)

    if serializer.is_valid() and not None:
        serializer.validated_data.pop('password', None)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_password(request):
    serializer = UpdatePasswordSerialzier(data=request.data, context={'request' : request})
    user = request.user
    if serializer.is_valid():
        user.set_password(serializer.validated_data['confirm_password'])
        user.save()
        return Response({"Message": "Password Changed Successfully."}, status=status.HTTP_200_OK)
    return Response({"user": user.username, "error" : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
