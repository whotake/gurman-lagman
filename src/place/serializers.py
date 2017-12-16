from rest_framework.serializers import ModelSerializer

from .models import Category, Place


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'parent',
            'name',
            'description'
        )


class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = (
            'id',
            'name',
            'description',
            'category'
        )
