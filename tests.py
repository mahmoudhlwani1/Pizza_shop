from rest_framework import serializers
from .models import Pizza	
class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'
from django.test import TestCase

# Create your tests here.
