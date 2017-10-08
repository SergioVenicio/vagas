# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagas',
            name='distancia_maxima',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vagas',
            name='faixa_salarial_max',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vagas',
            name='faixa_salarial_min',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
    ]
