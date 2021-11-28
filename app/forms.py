from django import forms

from .models import CryptoModel

class CryptoForm(forms.ModelForm):
    class Meta:
        model = CryptoModel
        fields = "__all__"