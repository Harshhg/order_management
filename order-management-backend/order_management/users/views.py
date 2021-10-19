
# Standard Library
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import BadRequest
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from order_management.users.serializers import AuthUserSerializer, LoginSerializer, RegisterSerializer


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]

    @action(methods=["POST"], detail=False)
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            raise BadRequest("Invalid username/password. Please try again!")

        response_serializer = AuthUserSerializer(user)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    @action(methods=["POST"], detail=False)
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get("email")
        user = User.objects.create_user(username=username, **serializer.validated_data)
        response_serializer = AuthUserSerializer(user)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
