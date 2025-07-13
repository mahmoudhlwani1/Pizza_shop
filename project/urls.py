from django.contrib import admin
from django.urls import path, include
from Task.views import TaskViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
urlpatterns = [
path('api/', include(router.urls)),
path('api-auth/', include('rest_framework.urls')),]
