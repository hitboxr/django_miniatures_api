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


class MiniPreviewSerializer(serializers.ModelSerializer):
    mini_images = MiniImageField(many=True, read_only=True)

    # TODO: Implement thumbnails for mini previews (aka refactor mini image handling again)

    class Meta:
        model = Mini
        fields = ['id', 'name', 'mini_images', 'added', 'modified', 'url']


class PackPreviewSerializer(serializers.ModelSerializer):
    pack_thumbnail = serializers.ImageField(use_url=True, read_only=True)

    class Meta:
        model = Pack
        fields = ['id', 'pack_name', 'pack_thumbnail', 'added', 'modified', 'url']


class MiniDetailSerializer(serializers.ModelSerializer):
    mini_images = MiniImageField(many=True, read_only=True)
    pack = PackPreviewSerializer(read_only=True)
    # size = serializers.CharField(source='get_size_display')

    class Meta:
        model = Mini
        fields = '__all__'

    # def to_representation(self, instance):
    #     mini = super().to_representation(instance)
    #     mini['size'] = Mini.Size(mini['size']).label
    #     return mini
    #


class PackDetailSerializer(serializers.ModelSerializer):
    pack_thumbnail = serializers.ImageField(use_url=True, read_only=True)
    minis = MiniPreviewSerializer(many=True, read_only=True)

    class Meta:
        model = Pack
        fields = '__all__'


class PackModifySerializer(serializers.ModelSerializer):
    minis = serializers.PrimaryKeyRelatedField(many=True, queryset=Mini.objects.all())

    class Meta:
        model = Pack
        fields = '__all__'
