from django.forms import ModelForm
from .models import websitedetail

class websitedetail(ModelForm):
    class Meta:
        model = websitedetail
        fields = '__all__'