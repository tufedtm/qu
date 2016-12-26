from django.views.generic import CreateView, ListView

from .models import Asd
from .forms import Foorm


class Create(CreateView, ListView):
    model = Asd
    template_name = 'first/asd.html'
    success_url = '/'
    form_class = Foorm
