from django.urls import path, include
from rest_framework import routers

from .views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path("index/", index),
    path('', include(router.urls)),
    path("users", UserView.as_view()),
]
