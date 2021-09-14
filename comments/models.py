from django.db import models
from news.models import News

class Comments(models.Model):
    new = models.ForeignKey(News, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=127, default='')
    text = models.TextField(max_length=127, default='')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.author_name
