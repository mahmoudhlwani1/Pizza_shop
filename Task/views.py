from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["size"]
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
    def get_queryset(self):
        return Task.objects.filter(name=self.request.user)