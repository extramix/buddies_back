from rest_framework.routers import DefaultRouter
from transactions.views.transaction import TransactionViewSet
from transactions.views.user import UserViewSet
from transactions.views.auth import AuthViewSet
from transactions.views.account import AccountViewSet
from transactions.views.category import CategoryViewSet


router = DefaultRouter()
router.register(r"transaction", TransactionViewSet, basename="transaction")
router.register(r"auth", AuthViewSet, basename="auth")
router.register(r"user", UserViewSet, basename="user")
router.register(r"account", AccountViewSet, basename="account")
router.register(r"category", CategoryViewSet, basename="category")

urlpatterns = router.urls
