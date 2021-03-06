from django import forms

from .models import CryptoModel, ContinuousTeadeModel

class CryptoForm(forms.ModelForm):
    class Meta:
        model = CryptoModel
        fields = ['min_lower_bound', 'max_upper_bound']

    # def validate(self, value):
    #     """Check if value consists only of valid emails."""
    #     # Use the parent's handling of required fields, etc.
    #     super().validate(value)
    #     for email in value:
    #         validate_email(email)
    
class ContinuousForm(forms.ModelForm):
    class Meta:
        model = ContinuousTeadeModel
        fields = ['volume24h', 'continuous_trade', "default_trade_time"]