from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from users.models import UserDetails
from users.forms import FtInField


class Post(models.Model):
    #fields here
    new_post = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    userdetails = UserDetails

    def __str__(self):
        return self.new_post[:10]


class Heart(models.Model):
    #fields here
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="heart_sent",
    )
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="heart_received",
    )
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.from_user} sent a Heart to {self.to_user} on {self.date_posted}.'


class updateInfo(models.Model):
    userdetails = UserDetails
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not_disclosed', 'Not Disclosed'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    userdetails = UserDetails
    date_of_birth = models.DateField()
    bio = models.TextField(blank=True)
    gender = models.CharField(
        max_length=13, choices=GENDER_CHOICES, default='male')

    def __str__(self):
        return f'{self.user.username}'
