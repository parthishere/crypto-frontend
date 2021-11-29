from django import forms

from .models import CryptoModel

class CryptoForm(forms.ModelForm):
    class Meta:
        model = CryptoModel
        fields = ['min_lower_bound', 'max_upper_bound']