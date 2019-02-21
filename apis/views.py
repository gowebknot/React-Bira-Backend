from django.contrib.auth.models import User
from rest_framework import viewsets

from apis.models import Issue
from apis.serializers import IssueSerializer
from apis.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=False).select_related('user_profile')
    serializer_class = UserSerializer


class IssuesViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all().select_related('assignee').select_related('created_by')
    serializer_class = IssueSerializer
