from rest_framework.viewsets import ModelViewSet
from comments.models import Comments
from comments.serializers import CommentSerializer

class CommentViewSet(ModelViewSet):

    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
