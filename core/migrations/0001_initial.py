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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Candidatos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('escolaridade', models.IntegerField(blank=True, null=True, choices=[(1, b'Fundamental incompleto'), (2, b'Fundamental completo'), (3, b'Ensino m\xc3\xa9dio incompleto'), (4, b'Ensino m\xc3\xa9dio completo'), (5, b'Ensino superior completo'), (6, b'Ensino superior incompleto')])),
                ('experiencia', models.IntegerField(null=True, blank=True)),
                ('distancia', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('faixa_salarial', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('senha', models.TextField(validators=[django.core.validators.MinLengthValidator(6)])),
            ],
        ),
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=255)),
                ('faixa_salarial_min', models.DecimalField(max_digits=10, decimal_places=2)),
                ('faixa_salarial_max', models.DecimalField(max_digits=10, decimal_places=2)),
                ('experiencia', models.IntegerField()),
                ('escolaridade', models.IntegerField(choices=[(1, b'Fundamental incompleto'), (2, b'Fundamental completo'), (3, b'Ensino m\xc3\xa9dio incompleto'), (4, b'Ensino m\xc3\xa9dio completo'), (5, b'Ensino superior completo'), (6, b'Ensino superior incompleto')])),
                ('distancia_maxima', models.DecimalField(max_digits=10, decimal_places=2)),
                ('candidatos', models.ManyToManyField(to='core.Candidatos', through='core.Candidato_Vaga', blank=True)),
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
