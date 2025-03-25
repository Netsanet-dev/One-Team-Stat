from rest_framework import serializers
from django.contrib.auth import get_user_model

MyUser = get_user_model()


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'password']

class UserProfileUpdate(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']

class UserPasswordChangeSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    class Meta:
        MyUser = MyUser
        fields = []

class UserRegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MyUser
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'role']
        extra_kwargs = {'password' : {'write_only': True}}

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        role = validated_data['role']
    
        user = MyUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=role
        )
        return user