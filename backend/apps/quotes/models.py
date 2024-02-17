from django.db import models


class Quote(models.Model):
    author = models.CharField(max_length=256)
    body = models.TextField()
    context = models.TextField()
    source = models.TextField(max_length=256)
    created_at = models.DateField(auto_now_add=True)

