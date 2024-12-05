from rest_framework import mixins, permissions, response, status
from rest_framework.viewsets import GenericViewSet

from src.base.mixins import ActionPermissionMixin
from src.base.permissions import IsAdmin, IsOwnerOrAdmin
from src.promotions.models import Promotion
from src.promotions.serializers import PromotionSerializer

from .models import TradingUser
from .serializers import UserProfileSerializer


class UserProfileViewSet(
    ActionPermissionMixin,
    GenericViewSet,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
):
    lookup_field = "pk"
    serializer_class = UserProfileSerializer
    permission_classes_by_action = {"retrieve": (IsOwnerOrAdmin,), "update": (IsAdmin,)}

    def get_queryset(self):
        return TradingUser.objects.filter(pk=self.kwargs.get("pk"))


class SubscribeOnPromotionListViewSet(
    GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin
):
    serializer_class = PromotionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Promotion.objects.filter(id=self.request.user.subscription_id)

    def create(self, request, *args, **kwargs):
        request.user.subscription_id = request.data.get("pk")
        request.user.save()
        return response.Response(
            "You've been subscribed on promotion", status=status.HTTP_200_OK
        )
