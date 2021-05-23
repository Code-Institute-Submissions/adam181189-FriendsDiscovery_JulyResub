from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django_countries.fields import CountryField
from djstripe.models import Customer, Subscription
from users.forms import FtInField

# https://www.youtube.com/watch?v=Tja4I_rgspI
# (used to understand how to change allauth as extended user)

# https://stackoverflow.com/questions/31130706/dropdown-in-django-model
# (used to understand dropdown)

# https://pypi.org/project/django-countries/#countryfield
# (used to understand built in nationality dropdown system)

# https://www.geeksforgeeks.org/imagefield-django-models/?ref=rp
# (used to understand how to add images)


# This is the database model for all users personal information
class UserDetails(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not_disclosed', 'Not Disclosed'),
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, null=True,
        blank=True, on_delete=models.CASCADE,
        related_name='userprofile')
    subscription = models.ForeignKey(
        Subscription, null=True, blank=True,
        on_delete=models.SET_NULL)
    # Other fields here
    premium_member = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=13, choices=GENDER_CHOICES, default='male')
    bio = models.TextField(blank=True, default='Let others know about you...')
    nationality = CountryField(
        blank_label='(select country)', default="Where are you from?")
    profile_pic = models.ImageField(
        upload_to="profile-image/", default='default.png', blank=True)
    received_hearts = models.IntegerField(default=0)
    daily_given_hearts = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username}'
