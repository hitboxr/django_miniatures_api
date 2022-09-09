from rest_framework import serializers
from .models import Mini, MiniImage, Pack


class MiniSerializer(serializers.ModelSerializer):
    images = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='url'
    )

    class Meta:
        model = Mini
        fields = ['id', 'name', 'description', 'added', 'modified', 'images']


class MiniImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniImage
        fields = '__all__'
