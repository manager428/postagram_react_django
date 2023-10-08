from rest_framework import routers
from core.user.viewsets import UserViewSet
from core.auth.viewsets import (RegisterViewSet)
router = routers.SimpleRouter()

router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')

urlpatterns = [
    *router.urls,
]
