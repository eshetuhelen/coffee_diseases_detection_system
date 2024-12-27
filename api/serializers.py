from rest_framework import serializers
from .models import CoffeeLeafImage

class CoffeeLeafImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeLeafImage
        fields = ['id', 'image', 'label']
