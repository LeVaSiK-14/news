from rest_framework.serializers import ModelSerializer
from news.models import News


class NewSerializer(ModelSerializer):

    class Meta:

        model = News
        fields = ['id', 'author_name', 'title', 'link', 'amount_of_upvotes']