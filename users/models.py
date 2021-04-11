from django.db import models
from django.contrib.auth.models import User

# https://www.youtube.com/watch?v=Tja4I_rgspI
# (used to understand how to change allauth as extended user)


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # https://stackoverflow.com/questions/31130706/dropdown-in-django-model 
    # (used to understand dropdown)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not_disclosed', 'Not Disclosed'),
    )

    # Other fields here
    premium_member = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=13, choices=GENDER_CHOICES, default='male')

    def __str__(self):
        return self.user.username

