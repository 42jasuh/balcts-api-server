# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (PostViewSet,
                    health_check)

router = DefaultRouter()

router.register('post', PostViewSet)

urlpatterns =[
    path('', include(router.urls)),
    path('health/', health_check),
]