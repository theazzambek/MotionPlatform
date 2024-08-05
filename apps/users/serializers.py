from rest_framework import serializers
from .models import MyUser, UserType
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'firstname', 'lastname', 'email', 'password', 'speciality', 'experience', 'role']

    def create(self, validated_data):
        user = MyUser(
            email=validated_data['email'],
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'],
            role=UserType.TEACHER,
            speciality=validated_data.get('speciality', ''),
            is_admin=validated_data.get('is_admin', False)
        )
        user.set_password(validated_data['password'])  # Используем set_password для хеширования пароля
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.speciality = validated_data.get('speciality', instance.speciality)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)
        if 'password' in validated_data:  # Проверяем, что пароль был изменен
            instance.set_password(validated_data['password'])  # Используем set_password для хеширования пароля
        instance.save()
        return instance

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

# class UserCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MyUser
#         fields = ('id', 'is_admin', 'role', 'password', 'firstname',
#                   'lastname', 'email', 'speciality', 'created_date', 'update_date')
#
#     def create(self, validated_data):
#         user = MyUser(**validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
#
#     def update(self, instance, validated_data):
#         for field, value in validated_data.items():
#             if field == 'password':
#                 instance.set_password(value)
#             else:
#                 setattr(instance, field, value)
#         instance.save()
#         return instance


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные.")
