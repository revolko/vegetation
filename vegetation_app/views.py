from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Plant
from .serializers import PlantSerializer


class PlantList(ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class PlantDetail(RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
