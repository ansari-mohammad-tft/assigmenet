from django.db import models

# Create your models here.
from django.db import models


class TopWordsModel(models.Model):
    topic = models.CharField(max_length=255, null=False, blank=False)
    top_words = models.JSONField(null=True)
    n = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic} - {self.created_at}"
