from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, \
    ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Category, Place
from .serializers import CategorySerializer, PlaceSerializer


class CategoryViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_fields = ('parent', )
    search_fields = ('name', 'description')


class PlaceViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_fields = ('category', )
    search_fields = ('name', 'description')
