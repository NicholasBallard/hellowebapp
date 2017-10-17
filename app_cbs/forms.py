from django.forms import ModelForm

from app_cbs.models import Thing

class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ('name', 'description',)