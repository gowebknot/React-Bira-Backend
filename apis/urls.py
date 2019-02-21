from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from apis.views import IssuesViewSet
from apis.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'issues', IssuesViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
