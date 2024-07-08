from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router_orders = DefaultRouter()

router_orders.register('orders', OrderViewSet, 'orders')