from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from .models import Image
from .serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.AllowAny]

@api_view(['GET'])
def getAllImages(request):
    images= Image.objects.all()
    return Response(ImageSerializer(images, many=True).data)

@api_view(['GET'])
def getById(request):
    images= Image.objects.get(id=request.GET.get('id'))
    return Response(ImageSerializer(images).data)