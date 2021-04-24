from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# https://www.youtube.com/watch?v=Tja4I_rgspI
# (used to understand how to change allauth as extended user)


class UserDetails(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not_disclosed', 'Not Disclosed'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # https://stackoverflow.com/questions/31130706/dropdown-in-django-model
    # (used to understand dropdown)

    # Other fields here
    premium_member = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=13, choices=GENDER_CHOICES, default='male')
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username
