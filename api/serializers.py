from rest_framework import serializers
from .models import Mini, MiniImage, Pack


class MiniImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, read_only=True)

    class Meta:
        model = MiniImage
        fields = ['image']


class MiniImageField(serializers.RelatedField):
    def to_representation(self, value):
        rel_path = serializers.ImageField(use_url=True, read_only=True).to_representation(value.image)
        return self.context.get('request').build_absolute_uri(rel_path)


class MiniSerializer(serializers.ModelSerializer):
    mini_images = MiniImageField(many=True, read_only=True)

    class Meta:
        model = Mini
        fields = '__all__'