from rest_framework import serializers
from .models import User


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'mobile')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'mobile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print("Data: ", validated_data)
        user = User.objects.create_user(validated_data['email'], validated_data['password'],
                                        validated_data['first_name'], validated_data['last_name'],
                                        validated_data['mobile'])

        return user

        # class ChangePasswordSerializer(serializers.ModelSerializer):
        #     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
        #     password2 = serializers.CharField(write_only=True, required=True)
        #     old_password = serializers.CharField(write_only=True, required=True)
        #
        #     class Meta:
        #         model = User
        #         fields = ('old_password', 'password', 'password2')
        #
        #     def validate(self, attrs):
        #         if attrs['password'] != attrs['password2']:
        #             raise serializers.ValidationError({"password": "Password fields didn't match."})
        #
        #         return attrs
        #
        #     def validate_old_password(self, value):
        #         user = self.context['request'].user
        #         if not user.check_password(value):
        #             raise serializers.ValidationError({"old_password": "Old password is not correct"})
        #         return value
        #
        #     def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
