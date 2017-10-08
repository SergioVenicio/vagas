# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MinLengthValidator

ESCOLARIDADE_CHOICES = (
    (1, 'Fundamental incompleto'),
    (2, 'Fundamental completo'),
    (3, 'Ensino médio incompleto'),
    (4, 'Ensino médio completo'),
    (5, 'Ensino superior completo'),
    (6, 'Ensino superior incompleto'),
)


class Empresas(models.Model):
    email = models.EmailField(unique=True)
    razao_social = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    ramo = models.CharField(max_length=255)
    numero = models.IntegerField()
    senha = models.TextField(validators=[MinLengthValidator(6)])


class Candidatos(models.Model):
    email = models.EmailField(unique=True)
    escolaridade = models.IntegerField(
        choices=ESCOLARIDADE_CHOICES, blank=True, null=True
    )
    experiencia = models.IntegerField(
        blank=True, null=True
    )
    distancia = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    faixa_salarial = models.DecimalField(
            max_digits=10, decimal_places=2, blank=True, null=True
    )
    senha = models.TextField(validators=[MinLengthValidator(6)])


class Vagas(models.Model):
    descricao = models.CharField(max_length=255)
    faixa_salarial_min = models.DecimalField(max_digits=8, decimal_places=2)
    faixa_salarial_max = models.DecimalField(max_digits=8, decimal_places=2)
    experiencia = models.IntegerField()
    escolaridade = models.IntegerField(
        choices=ESCOLARIDADE_CHOICES
    )
    distancia_maxima = models.DecimalField(max_digits=8, decimal_places=2)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    candidatos = models.ManyToManyField(
        Candidatos, blank=True, through='Candidato_Vaga'
    )


class Candidato_Vaga(models.Model):
    candidato = models.ForeignKey(Candidatos, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vagas, on_delete=models.CASCADE)
