from rest_framework import serializers
from .models import FoodData, FoodItem
from rest_framework.authtoken.models import Token

class FoodDataSerializer(serializers.ModelSerializer):

    class Meta:
        model= FoodItem
        fields = '__all__'
        depth = 2 


