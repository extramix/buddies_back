from rest_framework.routers import DefaultRouter
from transactions.views.transaction import TransactionViewSet


router = DefaultRouter()
router.register(r"transaction", TransactionViewSet, basename="transaction")

urlpatterns = router.urls
