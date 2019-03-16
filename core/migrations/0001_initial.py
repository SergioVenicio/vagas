# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato_Vaga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Candidatos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('escolaridade', models.IntegerField(blank=True, null=True, choices=[(1, 'Fundamental incompleto'), (2, 'Fundamental completo'), (3, 'Ensino médio incompleto'), (4, 'Ensino médio completo'), (5, 'Ensino superior completo'), (6, 'Ensino superior incompleto')])),
                ('experiencia', models.IntegerField(blank=True, null=True)),
                ('distancia', models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)),
                ('faixa_salarial', models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)),
                ('senha', models.TextField(validators=[django.core.validators.MinLengthValidator(6)])),
            ],
        ),
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('razao_social', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('ramo', models.CharField(max_length=255)),
                ('numero', models.IntegerField()),
                ('senha', models.TextField(validators=[django.core.validators.MinLengthValidator(6)])),
            ],
        ),
        migrations.CreateModel(
            name='Vagas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('descricao', models.CharField(max_length=255)),
                ('faixa_salarial_min', models.DecimalField(max_digits=8, decimal_places=2)),
                ('faixa_salarial_max', models.DecimalField(max_digits=8, decimal_places=2)),
                ('experiencia', models.IntegerField()),
                ('escolaridade', models.IntegerField(choices=[(1, 'Fundamental incompleto'), (2, 'Fundamental completo'), (3, 'Ensino médio incompleto'), (4, 'Ensino médio completo'), (5, 'Ensino superior completo'), (6, 'Ensino superior incompleto')])),
                ('distancia_maxima', models.DecimalField(max_digits=8, decimal_places=2)),
                ('candidatos', models.ManyToManyField(blank=True, to='core.Candidatos', through='core.Candidato_Vaga')),
                ('empresa', models.ForeignKey(to='core.Empresas')),
            ],
        ),
        migrations.AddField(
            model_name='candidato_vaga',
            name='candidato',
            field=models.ForeignKey(to='core.Candidatos'),
        ),
        migrations.AddField(
            model_name='candidato_vaga',
            name='vaga',
            field=models.ForeignKey(to='core.Vagas'),
        ),
    ]
