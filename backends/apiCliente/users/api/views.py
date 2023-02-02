from .serializers import CreateUserSerializer, UserSerializers, UserWriteSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin
)

from django.contrib.auth import get_user_model

User = get_user_model

class UserViewSet(CreateModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin):
    serialiser_class = UserWriteSerializer
    queryset =  User.objets.all()
