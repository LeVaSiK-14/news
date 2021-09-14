from rest_framework.viewsets import ModelViewSet
from news.models import News
from news.serializers import NewSerializer
from comments.serializers import CommentSerializer

from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from rest_framework import status
from comments.models import Comments

class NewViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewSerializer

    @action(methods=['get', ], detail=True)
    def annul_upvote(self, request, *agrs, **kwargs):
        new = self.get_object()
        if request.user.is_staff == True:
            new.amount_of_upvotes = 0
            new.save()            
            return Response({'Success': True})
        else:
            return Response({'Error': 'User is not admin'}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get', ], detail=True)
    def add_upvote(self, request, *agrs, **kwargs):
        new = self.get_object()
        new.amount_of_upvotes += 1 
        new.save()            
        return Response({'Success': True})

    @action(methods=['post', ], detail=True, serializer_class = CommentSerializer)
    def add_comment(self, request, *agrs, **kwargs):
        new = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            comment = Comments.objects.create(text=data['text'], new=new, author_name=data['author_name'], created_at=['created_at'])
            comment.save()
            return Response({'Success': True})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)