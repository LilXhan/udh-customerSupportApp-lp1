from rest_framework.routers import DefaultRouter
from .views import TicketModelViewSet

router_tickets = DefaultRouter()

router_tickets.register('tickets', TicketModelViewSet, 'tickets')