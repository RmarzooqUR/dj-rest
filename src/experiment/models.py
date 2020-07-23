from django.db import models
from django.contrib.auth import tokens
# Create your models here.
class Post(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title
