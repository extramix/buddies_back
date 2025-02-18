from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth.models import User
from transactions.serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework import permissions

from django.http import JsonResponse


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [SessionAuthentication]

    def get_permissions(self):
        # if self.action == "create" or self.action == "me":
        return [permissions.AllowAny()]
        # return super().get_permissions()

    @action(methods=["get"], detail=False)
    def me(self, request):
        if not request.user.is_authenticated:
            return JsonResponse(
                {
                    "name": "",
                    "username": "",
                    "email": "",
                }
            )
        return JsonResponse(
            {
                "name": request.user.get_full_name(),
                "username": request.user.username,
                "email": request.user.email,
            }
        )
