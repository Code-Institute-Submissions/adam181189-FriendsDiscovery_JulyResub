from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


class addPost(models.Model):
    #fields here
    new_post = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.new_post[:10]
