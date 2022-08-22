from django.forms import forms
from .models import Prospect

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Prospect
        fields = '__all__'