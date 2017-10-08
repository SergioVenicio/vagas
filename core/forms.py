# -*- coding: utf-8 -*-

from django import forms
from .models import Candidatos, Empresas, Vagas, ESCOLARIDADE_CHOICES
from django.core.validators import MinLengthValidator


class CandidatoForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu email'
            }
        )
    )
    senha = forms.CharField(
        validators=[MinLengthValidator(6)],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

    class Meta:
        model = Candidatos
        fields = ('email', 'senha')


class EditarCandidatoForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu email'
            }
        )
    )
    escolaridade = forms.ChoiceField(
        choices=ESCOLARIDADE_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Escolaridade'
            }
        )
    )
    experiencia = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Experiencia (Anos)'
            }
        )
    )
    distancia = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Distancia desejada até o trabalho (KM)'
            }
        ),
        localize=True
    )
    faixa_salarial = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Quanto deseja receber'
            }
        ),
        localize=True
    )

    senha = forms.CharField(
        validators=[MinLengthValidator(6)],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )
    Confirm_senha = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirme sua senha'
            }
        )
    )

    class Meta:
        model = Candidatos
        fields = ('__all__')


class EmpresaEditarCandidatoForm(forms.ModelForm):
        escolaridade = forms.ChoiceField(
            choices=ESCOLARIDADE_CHOICES,
            widget=forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escolaridade'
                }
            )
        )
        experiencia = forms.IntegerField(
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Experiencia (Anos)'
                }
            )
        )
        distancia = forms.DecimalField(
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Distancia até o trabalho (KM)'
                }
            ),
            localize=True
        )
        faixa_salarial = forms.DecimalField(
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Valor do salario'
                }
            ),
            localize=True
        )

        class Meta:
            model = Candidatos
            fields = (
                    'escolaridade', 'experiencia',
                    'distancia', 'faixa_salarial',
            )


class EmpresaForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o email'
            }
        )
    )
    razao_social = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a razão social'
            }
        )
    )
    endereco = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o endereço'
            }
        )
    )
    ramo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o ramo'
            }
        )
    )
    numero = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o numero'
            }
        )
    )
    senha = forms.CharField(
        validators=[MinLengthValidator(6)],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a senha'
            }
        )
    )

    class Meta:
        model = Empresas
        fields = ('__all__')


class EmpresaEditForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o email'
            }
        )
    )
    razao_social = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a razão social'
            }
        )
    )
    endereco = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o endereço'
            }
        )
    )
    ramo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o ramo'
            }
        )
    )
    numero = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o numero'
            }
        )
    )
    senha = forms.CharField(
        validators=[MinLengthValidator(6)],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a senha'
            }
        )
    )
    Confirm_senha = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirme a senha'
            }
        )
    )

    class Meta:
        model = Empresas
        fields = ('__all__')


class EmpresaLoginForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o email'
            }
        )
    )
    senha = forms.CharField(
        validators=[MinLengthValidator(6)],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a senha'
            }
        )
    )

    class Meta:
        model = Empresas
        fields = ('email', 'senha')


class VagaEmpresa(forms.ModelForm):
    descricao = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a descrição da vaga'
            }
        )
    )
    faixa_salarial_min = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Salário minimo'
            }
        ),
        localize=True
    )
    faixa_salarial_max = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Salário maximo'
            }
        ),
        localize=True
    )
    experiencia = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Experiencia (Anos)'
            }
        )
    )
    escolaridade = forms.ChoiceField(
        choices=ESCOLARIDADE_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Escolaridade'
            }
        )
    )
    distancia_maxima = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Distancia desejada até o trabalho (KM)'
            }
        ),
        localize=True
    )

    class Meta:
        model = Vagas
        fields = (
                'descricao', 'faixa_salarial_min', 'faixa_salarial_max',
                'experiencia', 'escolaridade', 'distancia_maxima'
        )
