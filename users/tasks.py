from celery import shared_task
from .models import UserDetails

import time

@shared_task
def reset_hearts_at_midnight():
    UserDetails.objects.update(daily_given_hearts=0)
