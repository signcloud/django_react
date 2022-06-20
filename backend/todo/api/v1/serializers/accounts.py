from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'mobile')

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['password'],
                                        validated_data['first_name'], validated_data['last_name'],
                                        validated_data['mobile'])
        return user