from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from api.v1.views import UserViewSet, api_root


router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', api_root),
    path('', include(router.urls))
]
