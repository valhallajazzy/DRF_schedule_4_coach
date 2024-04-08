from rest_framework import viewsets

from schedule_api.models import Client
from schedule_api.serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()