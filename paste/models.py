from django.contrib.auth.models import User
from django.db import models


class TextFile(models.Model):
    author = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.text[:50]
