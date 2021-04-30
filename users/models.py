from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django_countries.fields import CountryField

# https://www.youtube.com/watch?v=Tja4I_rgspI
# (used to understand how to change allauth as extended user)


class UserDetails(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not_disclosed', 'Not Disclosed'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

    # https://stackoverflow.com/questions/31130706/dropdown-in-django-model
    # (used to understand dropdown)

    # https://pypi.org/project/django-countries/#countryfield
    # (used to understand built in nationality dropdown system)

    # Other fields here
    premium_member = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=13, choices=GENDER_CHOICES, default='male')
    bio = models.TextField(blank=True, default='Let others know about you...')
    nationality = CountryField(
        blank_label='(select country)', default="Where are you from?")
    profile_pic = models.ImageField(
        default='default.png', blank=True)

    def __str__(self):
        return f'{self.user.username}'
