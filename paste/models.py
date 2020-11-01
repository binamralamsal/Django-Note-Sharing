from django.contrib.auth.models import User
from django.db import models


class TextFile(models.Model):
    class Meta:
        ordering = ('-time',)

    privacy = (
        ('PRIVATE', 'Private'),
        ('PUBLIC', 'Public')
    )
    author = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    text = models.TextField()
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    time = models.DateTimeField(auto_now=True)
    expiration_date = models.DateField(null=True, blank=True)
    key = models.CharField(blank=True, null=True, max_length=20)
    security = models.TextField(choices=privacy, default='PUBLIC')

    def __str__(self):
        return self.title
