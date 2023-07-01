from django.conf import settings
from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
    image = models.FileField(upload_to='user/images')
    description = models.CharField(max_length=120)
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.image} + {self.description}'
