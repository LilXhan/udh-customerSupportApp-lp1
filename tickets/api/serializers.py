from rest_framework.serializers import ModelSerializer
from users.api.serializers import UserSerializer
from ..models import Ticket

class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'asunto', 'descripcion', 'canal', 'grupo', 'creado_el', 'actualizado_el', 'estado', 'usuario']