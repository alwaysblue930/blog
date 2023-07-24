from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(default='default title', max_length = 100)
    body = models.CharField(default='default body', max_length = 1000000)
    create_at = models.DateTimeField(auto_now_add=True)
