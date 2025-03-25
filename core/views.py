# from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from .permissions import IsCoachUser, IsRegularUser, IsPlayerUser,IsAdminUser
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserProfileUpdate, 
    UserPasswordChangeSerializer
)


# Get the Custom User Model
MyUser = get_user_model()


# Access and refresh token for a requested user
def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh' : str(refresh),
        'access' : str(refresh.access_token)
    }


@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def register_user(request):
    """
    User Registration
    """
    serializer = UserRegistrationSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        token = get_token_for_user(user)
        return Response({'user':serializer.data, 'token': token}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({'error' : "Invalid Account"})

    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        token = get_token_for_user(user)
        user_serilaizer = UserLoginSerializer(user)
        return Response({'user': user_serilaizer.data, 'token': token}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid'},status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response({'message': 'Logout Successful'}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'refresh token': f'{refresh_token}'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsPlayerUser])
def protected_view(request):
    user = request.user
    return Response({"Message": f"{user.username} Congratulations You are seeing this."})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_info(request):
    user = request.user
    serializer = UserProfileUpdate(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.validated_data.pop('password', None)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)