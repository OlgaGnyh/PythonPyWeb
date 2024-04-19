from django.shortcuts import render
from apps.route.models import Routes
from .serializers import RoutesSerializer, RoutesModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin


class RoutesGenericAPIView(GenericAPIView, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin,
                           DestroyModelMixin):
    queryset = Routes.objects.all()
    serializer_class = RoutesModelSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get(self.lookup_field):  # если был передан id или pk
            # возвращаем один объект
            return self.retrieve(request, *args, **kwargs)
        # Иначе возвращаем список объектов
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class RoutesViewSet(ModelViewSet):
    queryset = Routes.objects.all()
    serializer_class = RoutesModelSerializer

    @action(detail=True, methods=['post'])
    def my_action(self, request, pk=None):
        # Ваша пользовательская логика здесь
        return Response({'message': f'Пользовательская функция для пользователя с pk={pk}'})


