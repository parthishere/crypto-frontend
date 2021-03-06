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

class ContinuousTeadeModel(models.Model):
    continuous_trade = models.BooleanField(default=False)
    volume24h = models.FloatField(default=1000)
    default_trade_time = models.FloatField(default=2, verbose_name="estimated in hours")
    
class ContractTradeModel(models.Model):
    crypto_name = models.CharField(choices=CRYPTO_CHOICES, max_length=4, default='CTS')
    time = models.DateField(auto_now_add=True)
    trade_volume = models.FloatField(null=True, blank=True)