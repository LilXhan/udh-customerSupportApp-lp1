from rest_framework.viewsets import ModelViewSet
from ..models import Ticket
from .serializers import TicketSerializer
from .permissions import TicketsPermissions

class TicketModelViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [TicketsPermissions]

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            queryset = Ticket.objects.all()
            return queryset
        else:
            user = self.request.user
            queryset = Ticket.objects.filter(usuario=user.id)
            return queryset