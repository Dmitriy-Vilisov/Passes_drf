from rest_framework.response import Response
from rest_framework import generics, viewsets
from .models import Pereval_added
from .serializers import Pereval_addedSerializer, PerevalSerializer
import django_filters


class Pereval_addedAPICreate(generics.CreateAPIView):  # submitData
    queryset = Pereval_added.objects.all()
    serializer_class = Pereval_addedSerializer


class PerevalOne(generics.RetrieveUpdateAPIView):
    queryset = Pereval_added.objects.all()
    serializer_class = Pereval_addedSerializer

    def patch(self, request, pk):
        try:
            pereval = Pereval_added.objects.get(id=pk)
            if pereval.status != 'new':
                return Response({"state": 0, "message": "Нельзя редактировать запись,"
                                                        " не находящуюся в статусе 'new'"}, status=400)
            # чтобы отредактировать запись, нужно удалить user из отсылаемого json'a
            if 'user' in request.data:
                return Response({"state": 0, "message": "Нельзя редактировать поле 'user'"}, status=400)
            serializer = Pereval_addedSerializer(pereval, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"state": 1, "message": "Запись успешно отредактирована"})
            else:
                return Response({"state": 0, "message": "Ошибка валидации данных"}, status=400)
        except Pereval_added.DoesNotExist:
            return Response({"state": 0, "message": "Перевал не найден"}, status=404)


class PerevalByUserEmailList(viewsets.ModelViewSet):
    queryset = Pereval_added.objects.all()
    serializer_class = Pereval_addedSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["user__email"]

class PerevalViewSet(viewsets.ModelViewSet):  # проверяем
    queryset = Pereval_added.objects.all()
    serializer_class = PerevalSerializer
