from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other fields here
    premium_member = models.BooleanField(default=False)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user.username

