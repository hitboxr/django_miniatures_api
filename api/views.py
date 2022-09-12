from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from .models import Mini, MiniImage
from .serializers import MiniSerializer, MiniImageSerializer

# Create your views here.


class MiniListAPIView(ListCreateAPIView):
    queryset = Mini.objects.prefetch_related('mini_images')
    serializer_class = MiniSerializer
    parser_classes = [FormParser, MultiPartParser]

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
    serializer_class = MiniSerializer


@api_view(['GET', 'POST'])
def pack_list(request):
    pass


@api_view(['GET', 'PUT', 'DELETE'])
def pack_detail(request):
    pass
