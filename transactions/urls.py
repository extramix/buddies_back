from rest_framework.routers import DefaultRouter
from transactions.views.transaction import TransactionViewSet
from transactions.views.user import UserViewSet
from transactions.views.auth import AuthViewSet


router = DefaultRouter()
router.register(r"transaction", TransactionViewSet, basename="transaction")
router.register(r"auth", AuthViewSet, basename="auth")
router.register(r"user", UserViewSet, basename="user")

urlpatterns = router.urls
