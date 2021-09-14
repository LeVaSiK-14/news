from rest_framework.routers import SimpleRouter

from comments.views import CommentViewSet

router = SimpleRouter()

router.register('comments', CommentViewSet)

urlpatterns = []

urlpatterns += router.urls
