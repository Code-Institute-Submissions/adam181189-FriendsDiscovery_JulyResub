from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from users.models import UserDetails

class Post(models.Model):
    #fields here
    new_post = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    userdetails = UserDetails
    ## select users_userdetails.user_id == auth_user.id

    def __str__(self):
        return self.new_post[:10]
