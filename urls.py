from django.urls import path, include
from orders.views import OrderViewSet                                                                
from rest_framework.routers import DefaultRouter                                             
router = DefaultRouter()                                                                                          
router.register(r'orders', OrderViewSet)                                                                
urlpatterns = [                                                                                                         
    path('api/', include(router.urls)),                                                         
    path('api-auth/', include('rest_framework.urls')),  ]                            
