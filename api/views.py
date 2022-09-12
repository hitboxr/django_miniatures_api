from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from .models import Mini, MiniImage
from .serializers import MiniSerializer, MiniImageSerializer

# Create your views here.


# @api_view(['GET', 'POST'])
# @parser_classes([FormParser, MultiPartParser])
# def mini_list(request):
#     """
#     List all miniatures, or create a new miniature.
#     """
#     if request.method == 'GET':
#         miniatures = Mini.objects.prefetch_related('images')
#         serializer = MiniSerializer(miniatures, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = MiniSerializer(request.data)
#         if serializer.is_valid():
#             images = request.FILES.getlist('image')
#             mini_obj = serializer.save()
#             for i in images:
#                 # TODO: error checking for images? it's not handled by the mini serializer.
#                 #  Maybe make a separate image serializer that's only used for incoming?
#                 #MiniImage.objects.create(mini=mini_obj, image=i)
#                 image_serializer = MiniImageSerializer(mini=mini_obj, image=i)
#                 if image_serializer.is_valid():
#                     image_serializer.save()
#                 else:
#                     return Response(image_serializer.errors, status.HTTP_400_BAD_REQUEST)
#             return Response(request.POST, status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#     # TODO: Try running this and find out if we need two serializers, one with image
#     #  urls as an extra field(for outgoing) and one without them for writing incoming
#     #  new minis (and handling the images outside the serializer)

class MiniListAPIView(ListCreateAPIView):
    queryset = Mini.objects.prefetch_related('mini_images')
    serializer_class = MiniSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def mini_detail(request, pk):
    pass


@api_view(['GET', 'POST'])
def pack_list(request):
    pass


@api_view(['GET', 'PUT', 'DELETE'])
def pack_detail(request):
    pass
