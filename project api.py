from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer  # تم إزالة الأقواس () لأننا نريد إشارة إلى الكلاس وليس استدعاءه
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'pizza__size']
    
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)