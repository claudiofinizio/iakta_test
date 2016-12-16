from datetime import datetime

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    what = models.CharField(max_length=200, null=True, blank=True)
    when = models.DateTimeField(
        auto_now=False, 
        auto_now_add=False,
        null=True,
        blank=True,
    )
        
    def __str__(self):
        return self.title