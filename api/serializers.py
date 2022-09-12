from rest_framework import serializers
from .models import Mini, MiniImage, Pack


class MiniImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, read_only=True)

    class Meta:
        model = MiniImage
        fields = ['image']


class MiniSerializer(serializers.ModelSerializer):
    mini_images = MiniImageSerializer(many=True)

    class Meta:
        model = Mini
        fields = ['name', 'description', 'added', 'modified', 'mini_images']

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        mini = Mini.objects.create(**validated_data)
        for image in images_data:
            MiniImage.objects.create(mini=mini, **image)

        return mini
