from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"", views.AutoOrderViewSet, basename="autoorder")

urlpatterns = router.urls
