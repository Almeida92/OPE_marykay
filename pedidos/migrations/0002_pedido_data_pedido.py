# Generated by Django 2.0.5 on 2018-11-24 19:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='data_pedido',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]