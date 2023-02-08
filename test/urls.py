from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TestMVS

router = DefaultRouter()
router.register(r'test', TestMVS)

urlpatterns = router.urls

# urlpatterns = [
#     path(),
# ]