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

    def get_permissions(self):
        if self.action == 'me':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        # allow only admin to list users
        if not request.user.is_superuser:
            raise PermissionDenied("This action is not allowed")
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied("This action is not allowed")
        return super().retrieve(request, *args, **kwargs)

    @action(methods=["get"], detail=False)
    def me(self, request):
        return JsonResponse(
            {
                "name": request.user.get_full_name(),
                "username": request.user.username,
                "email": request.user.email,
            }
        )
