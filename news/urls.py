from rest_framework.routers import SimpleRouter

from news.views import NewViewSet

router = SimpleRouter()

router.register('news', NewViewSet)

urlpatterns = []

urlpatterns += router.urls
