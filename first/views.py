from django.http import HttpResponse

from .tasks import asd
from .models import Asd


def index(request):
    asd.delay()
    return HttpResponse(Asd.objects.count())
