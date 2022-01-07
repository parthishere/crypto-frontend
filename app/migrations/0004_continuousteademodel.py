# Generated by Django 3.2.9 on 2022-01-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211129_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContinuousTeadeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continuous_trade', models.BooleanField(default=False)),
                ('volume24h', models.FloatField(default=1000)),
            ],
        ),
    ]
