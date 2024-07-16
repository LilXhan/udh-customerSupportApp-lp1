from rest_framework.viewsets import ModelViewSet

from ..models import Order
from .serializers import OrderSerializer

from .permissions import OrdersPermissions

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [OrdersPermissions]
    
    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            queryset = Order.objects.all()
            return queryset
        else:
            user = self.request.user
            queryset = Order.objects.filter(usuario=user.id)
            return queryset