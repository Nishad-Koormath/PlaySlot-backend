from rest_framework import serializers
from .models import Turf, TurfImage

class TurfImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurfImage
        fields = ['id', 'image']
        
class TurfSerializer(serializers.ModelSerializer):
    images = TurfImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False), 
        write_only=True, required=False)
    
    class Meta:
        model = Turf
        fields = [
            'id', 'owner', 'name', 'location', 'description', 'day_price_per_hour', 'night_price_per_hour',
            'day_start_time', 'night_start_time', 'is_active', 'created_at', 'updated_at', 'images', 'uploaded_images'
        ]
        read_only_fields = ['owner', 'created_at', 'updated_at'] 
    
    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])        
        turf = Turf.objects.create(**validated_data)
        for image in uploaded_images:
            TurfImage.objects.create(turf=turf, image=image)
        return turf