# Generated by Django 2.0.5 on 2018-10-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='descricao',
            field=models.CharField(default='', max_length=100),
        ),
    ]
