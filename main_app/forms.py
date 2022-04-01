from django.forms import ModelForm
from .models import Watched

 
class WatchedForm(ModelForm):
    class Meta:
        model = Watched
        fields = ['date', 'review']