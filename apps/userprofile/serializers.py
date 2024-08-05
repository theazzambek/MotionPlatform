from rest_framework import serializers
from .models import Profile
from django.contrib.auth import get_user_model
from apps.users.serializers import MyUserSerializer

MyUser = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    user = MyUserSerializer(read_only=True)
    cover_url = serializers.ImageField(source='cover', read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'cover_url']
