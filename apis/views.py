from django.contrib.auth.models import User
from django_filters import FilterSet
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter

from apis.models import Issue
from apis.serializers import IssueSerializer
from apis.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=False).select_related('user_profile')
    serializer_class = UserSerializer


class IssueFilter(FilterSet):
    created_date = filters.DateFromToRangeFilter(field_name="created_at")
    updated_date = filters.DateFromToRangeFilter(field_name="updated_at")

    class Meta:
        model = Issue
        fields = {
            'short_id': ['exact'],
            'priority': ['exact', 'in'],
            'status': ['exact', 'in'],
            'assignee': ['exact'],
        }


class IssuesViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all().select_related('assignee').select_related('created_by')
    serializer_class = IssueSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('title',)
    filter_class = IssueFilter
    ordering = ('id',)
    ordering_fields = ('created_at', 'updated_at',)
