from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.http import JsonResponse
from rest_framework import permissions
from transactions.serializers import LoginSerializer
from django.middleware.csrf import get_token


class AuthViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @method_decorator(csrf_protect)
    @action(methods=["post"], detail=False)
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(request, **serializer.validated_data)
        print(serializer)
        if not user:
            return JsonResponse(
                {"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
            )

        login(request, user)
        return JsonResponse(
            {
                "name": user.get_full_name(),
                "username": user.username,
                "email": user.email,
            },
            status=status.HTTP_200_OK,
        )

    @action(methods=["get"], detail=False)
    def csrf_token(self, request):
        return JsonResponse({"token": get_token(request)}, status=status.HTTP_200_OK)
