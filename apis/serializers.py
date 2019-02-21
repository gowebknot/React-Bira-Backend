from django.contrib.auth.models import User
from rest_framework import serializers

from apis.models import Issue


class UserSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    profile_pic = serializers.SerializerMethodField()

    def get_title(self, user):
        if hasattr(user, "user_profile"):
            return user.user_profile.title
        return None

    def get_profile_pic(self, user):
        if hasattr(user, "user_profile"):
            return user.user_profile.profile_pic
        return None

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'title', 'profile_pic')


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('__all__')