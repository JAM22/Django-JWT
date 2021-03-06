from django.urls import include, path, re_path
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    re_path(r'', include(router.urls)),
]

