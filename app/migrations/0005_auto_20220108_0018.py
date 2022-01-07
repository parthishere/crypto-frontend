# Generated by Django 3.2.9 on 2022-01-07 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_continuousteademodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='continuousteademodel',
            name='default_trade_time',
            field=models.FloatField(default=24, verbose_name='estimated in minutes'),
        ),
        migrations.AlterField(
            model_name='contracttrademodel',
            name='crypto_name',
            field=models.CharField(choices=[('BTC', 'BTC'), ('CTS', 'CTS'), ('ETH', 'ETH')], default='CTS', max_length=4),
        ),
        migrations.AlterField(
            model_name='cryptomodel',
            name='crypto_name',
            field=models.CharField(choices=[('BTC', 'BTC'), ('CTS', 'CTS'), ('ETH', 'ETH')], default='CTS', max_length=4),
        ),
    ]
