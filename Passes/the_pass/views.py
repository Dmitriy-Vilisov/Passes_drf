from rest_framework import generics, viewsets
from .models import Pereval_added
from .serializers import Pereval_addedSerializer, PerevalSerializer


class Pereval_addedAPICreate(generics.CreateAPIView):  # submitData
    queryset = Pereval_added.objects.all()
    serializer_class = Pereval_addedSerializer


class PerevalViewSet(viewsets.ModelViewSet):  # проверяем
    queryset = Pereval_added.objects.all()
    serializer_class = PerevalSerializer
