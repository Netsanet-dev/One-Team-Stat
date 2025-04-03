from rest_framework import serializers
from django.contrib.auth import get_user_model


MyUser = get_user_model()


class UpdatePasswordSerialzier(serializers.ModelSerializer):
    password = serializers.CharField(help_text="Old Passowrd", write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = MyUser
        fields = ['password', 'new_password', 'confirm_password']

    def validate(self, data):
        # Check if the new password is the same as confirm password
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords don't match")
        
        # Get the request user
        request = self.context.get('request')
        user = request.user

        # Check if the user old password is the same as password
        if not user.check_password(data['password']):
            raise serializers.ValidationError('Incorrect Old Password')
        return data
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data['confirm_password'])
        instance.save()
        return instance

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'password']

class UserProfileUpdate(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'role']
        extra_kwargs = {"password": {"write_only":True, "required": False}}


class UserRegistrationSerializer(serializers.ModelSerializer):  
    class Meta:
        model = MyUser
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password' : {'write_only': True}}

    def create(self, validated_data): 
        user = MyUser.objects.create_user(**validated_data)
        return user