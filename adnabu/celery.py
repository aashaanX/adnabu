import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adnabu.settings')

app = Celery('adnabu')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()