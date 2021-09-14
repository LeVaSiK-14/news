from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class News(models.Model):
    author_name = models.CharField(max_length=127, default='')
    title = models.CharField(max_length=127, default='')
    link = models.URLField(max_length=255, default='', null=True)
    created_at = models.DateField(auto_now_add=True)
    amount_of_upvotes = models.PositiveIntegerField(default=0, max_length=127)
    
    def __str__(self):
        return self.author_name + self.title