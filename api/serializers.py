from rest_framework import serializers
import base64
from .models import CoffeeLeafImage

class CoffeeLeafImageSerializer(serializers.ModelSerializer):
    image_base64 = serializers.SerializerMethodField()

    class Meta:
        model = CoffeeLeafImage
        fields = ['id', 'name', 'image_base64']

    def get_image_base64(self, obj):
        # Directly use the binary field in obj.image
        return base64.b64encode(obj.image).decode('utf-8')
