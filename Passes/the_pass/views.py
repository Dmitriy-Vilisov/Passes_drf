from rest_framework import generics, viewsets
from .models import Pereval_added
from .serializers import PerevalSerializer, Pereval_addedSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval_added.objects.all()
    serializer_class = PerevalSerializer


class Pereval_addedAPICreate(generics.CreateAPIView):  # submitData
    queryset = Pereval_added.objects.all()
    serializer_class = Pereval_addedSerializer