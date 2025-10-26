from rest_framework.routers import DefaultRouter
from .views import TurfViewSet

router = DefaultRouter()
router.register(r'turfs', TurfViewSet, basename='turf')

urlpatterns = router.urls