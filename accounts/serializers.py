from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','password']


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email','username','password','first_name','last_name')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        user = User.objects.create_user(email=email, password=password, **validated_data)
        return user
