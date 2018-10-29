import string

import time
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery.decorators import task


@task()
def extract_async(urequest):
    urequest.extract_contents()

    
