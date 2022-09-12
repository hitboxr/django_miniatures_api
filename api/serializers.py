from rest_framework import serializers
from .models import Mini, MiniImage, Pack


class MiniImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, read_only=True)

    class Meta:
        model = MiniImage
        fields = ['image']


class MiniSerializer(serializers.ModelSerializer):
    mini_images = MiniImageSerializer(many=True, read_only=True)

    class Meta:
        model = Mini
        fields = ['name', 'description', 'added', 'modified', 'mini_images']
