from rest_framework.viewsets import ModelViewSet
from ..models import Ticket
from .serializers import TicketSerializer
from .permissions import IsAdminOrReadOnly

class TicketModelViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        queryset = Ticket.objects.filter(usuario=user.id)

        return queryset
    
    lookup_field = 'user'