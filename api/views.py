from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from .models import Mini, MiniImage, Pack
from .serializers import MiniImageSerializer, MiniDetailSerializer, MiniPreviewSerializer, \
                         PackPreviewSerializer, PackDetailSerializer, PackModifySerializer

# Create your views here.


class MiniListAPIView(ListCreateAPIView):
    queryset = Mini.objects.prefetch_related('mini_images')
    parser_classes = [FormParser, MultiPartParser]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MiniDetailSerializer
        return MiniPreviewSerializer

    def post(self, request, *args, **kwargs):
        image_data = request.FILES.getlist('mini_images')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        for image in image_data:
            image_serializer = MiniImageSerializer(data={'image': image})
            image_serializer.is_valid(raise_exception=True)
        mini_obj = serializer.save()
        for image in image_data:
            MiniImage.objects.create(mini=mini_obj, image=image)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=self.get_success_headers(serializer.data))


class MiniDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Mini.objects.prefetch_related('mini_images')
    serializer_class = MiniDetailSerializer


class PackListAPIView(ListCreateAPIView):
    queryset = Pack.objects.prefetch_related('minis')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PackModifySerializer
        return PackPreviewSerializer


class PackDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Pack.objects.prefetch_related('minis')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PackDetailSerializer
        if self.request.method == 'PUT' or 'PATCH':
            return PackModifySerializer
        return PackDetailSerializer
