from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'friendsdiscovery.settings')

app = Celery('friendsdiscovery')

app.config_from_object('django.conf:settings', namespace='CELERY')

broker_url = 'amqp://myuser:mypassword@localhost:5672/myvhost'

app.conf.beat_schedule = {
    'add-every-day': {
        'task': 'users.tasks.reset_hearts_at_midnight',
        'schedule': crontab(),
        'args': (16, 16)
    },
}
app.conf.timezone = 'GMT'

app.autodiscover_tasks()