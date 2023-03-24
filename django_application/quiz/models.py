from django.db import models


# Create your models here.
class Quiz(models.Model):
    title = models.CharField(
        max_length=200
    )

    body = models.TextField()

    answer = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False
    )