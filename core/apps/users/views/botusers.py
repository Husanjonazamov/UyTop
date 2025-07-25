from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.apps.users.models import BotusersModel
from core.apps.users.serializers.botusers import (
    CreateBotusersSerializer,
    ListBotusersSerializer,
    RetrieveBotusersSerializer,
)


@extend_schema(tags=["botusers"])
class BotusersView(BaseViewSetMixin, ModelViewSet):
    queryset = BotusersModel.objects.all()
    serializer_class = ListBotusersSerializer
    permission_classes = [IsAuthenticated]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBotusersSerializer,
        "retrieve": RetrieveBotusersSerializer,
        "create": CreateBotusersSerializer,
    }
