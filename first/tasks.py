from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .models import Asd


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def asd():
    for item in range(100000000000000):
        xx = Asd(ti=item)
        xx.save()
