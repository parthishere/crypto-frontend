from django.db import models

# Create your models here.

CRYPTO_CHOICES  = {
    ('CTS', 'CTS'),
    ('BTC', 'BTC'),
    ('ETH', 'ETH'),
}

class CryptoModel(models.Model):
    crypto_name = models.CharField(choices=CRYPTO_CHOICES, max_length=4, default='CTS')
    current_value = models.FloatField(default=0.0)
    max_upper_bound = models.FloatField(null=True, blank=True)
    min_lower_bound = models.FloatField(null=True, blank=True)
    
class ContractTradeModel(models.Model):
    crypto_name = models.CharField(choices=CRYPTO_CHOICES, max_length=4, default='CTS')
    time = models.DateField(auto_now_add=True)
    trade_volume = models.FloatField(null=True, blank=True)