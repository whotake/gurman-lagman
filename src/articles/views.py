from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, \
    ListModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_fields = ('place', )
    search_fields = ('title', 'body')
