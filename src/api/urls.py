from rest_framework import routers

from articles.views import ArticleViewSet
from place.views import CategoryViewSet, PlaceViewSet

router = routers.SimpleRouter()

router.register(r'article', ArticleViewSet, base_name='article')
router.register(r'category', CategoryViewSet, base_name='category')
router.register(r'place', PlaceViewSet, base_name='place')

app_name = 'api'
urlpatterns = [
]

urlpatterns += router.urls
