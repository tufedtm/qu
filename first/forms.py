from django import forms

from .models import Asd
from .tasks import asd


class Foorm(forms.ModelForm):
    class Meta:
        model = Asd
        fields = ['co']

    def save(self, commit=True):
        qwe = super(Foorm, self).save(commit=True)
        asd.delay(qwe.id)
        return super(Foorm, self).save(commit=True)
