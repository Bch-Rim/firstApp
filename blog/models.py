from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):   
    author         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title          = models.CharField(max_length=200)
    text           = models.TextField()
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
