import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flatgov.settings.dev')

app = Celery('flatgov')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.redbeat_redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
app.conf.broker_pool_limit = 1
app.conf.broker_heartbeat = None
app.conf.broker_connection_timeout = 30
app.conf.worker_prefetch_multiplier = 1

app.conf.beat_schedule = {
    'update_bill': {
        'task': 'uscongress.tasks.update_bill_task',
        'schedule': crontab(minute=0, hour=0),
        # 'schedule': crontab(),
        'options': {'queue': 'bill'}
    }
}

app.conf.timezone = 'UTC'