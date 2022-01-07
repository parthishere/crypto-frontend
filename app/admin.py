from django.contrib import admin

from .models import CryptoModel, ContinuousTeadeModel

# Register your models here.
admin.site.register(CryptoModel)
admin.site.register(ContinuousTeadeModel)