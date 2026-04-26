from django.db import models
from django.contrib.auth.models import User


class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.TextField()
    result = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url