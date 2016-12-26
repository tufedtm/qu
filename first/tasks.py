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
def asd(item_id):
    item = Asd.objects.get(id=item_id)
    for i in range(item.co):
        item.ti += 1
        item.save()
