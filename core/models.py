# -*- coding: utf-8 -*-
import hashlib
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


def HashPassword(senha=None):
    if senha:
        senha = hashlib.sha512(u'{}'.format(senha).encode('utf-8')).hexdigest()
        return senha
    else:
        return False


class Empresas(models.Model):
    email = models.EmailField(unique=True)
    razao_social = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    ramo = models.CharField(max_length=255)
    numero = models.IntegerField()
    senha = models.TextField(validators=[MinLengthValidator(6)])

    def login_empresa(self, request=None, email=None, senha=None):
        if not request.session.get('email_empresa', None):
            self.email = email
            self.senha = HashPassword(senha)
            try:
                self.empresa = Empresas.objects.get(
                    email=self.email, senha=self.senha
                )

                if request.session.get('email', False):
                    del request.session['email']
                if request.session.get('id', False):
                    del request.session['id']
                if request.session.get('candidato'):
                    del request.session['candidato']

                request.session['email_empresa'] = self.empresa.email
                request.session['id_empresa'] = self.empresa.id
                request.session['empresa'] = True
                return self.empresa
            except Empresas.DoesNotExist:
                return False
        else:
            return False

    def empresa_update(self, id=None, email=None, razao_social=None,
                       endereco=None, ramo=None, numero=None, senha=None):
        if id:
            self.empresa = self.get_empresa_by_id(id=id)
            if self.empresa:
                if senha:
                    self.empresa.senha = HashPassword(senha)
                self.empresa.email = email
                self.empresa.razao_social = razao_social
                self.empresa.endereco = endereco
                self.empresa.ramo = ramo
                self.empresa.numero = numero
                self.empresa.save()
                return True
        else:
            return False

    def get_empresa_by_id(self, id=id):
        if id:
            self.id = id
            try:
                self.empresa = Empresas.objects.get(pk=self.id)
                return self.empresa
            except Empresas.DoesNotExist:
                return False
        else:
            return False


def CheckLogin(request):
    email_candidato = request.session.get('email', False)
    email_empresa = request.session.get('email_empresa', False)

    if email_candidato or email_empresa:
        return True
    else:
        return False


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

    def login(self, request, email=None, senha=None):
        self.email = email
        self.senha = HashPassword(senha)

        if not request.session.get('email', False):
            try:
                self.candidato = Candidatos.objects.get(
                    email=self.email, senha=self.senha
                )
                if request.session.get('email_empresa', False):
                    del request.session['email_empresa']
                if request.session.get('id_empresa', False):
                    del request.session['id_empresa']
                if request.session.get('empresa', False):
                    del request.session['empresa']

                request.session['email'] = self.candidato.email
                request.session['id'] = self.candidato.id
                request.session['candidato'] = True
                return self.candidato
            except Candidatos.DoesNotExist:
                return False
        else:
            return True

    def candidato_update(self, id=None, email=None, escolaridade=None,
                         experiencia=None, distancia=None,
                         faixa_salarial=None, senha=None):
        if id:
            self.id = id
            self.distancia = distancia
            self.faixa_salarial = faixa_salarial
            self.candidato = self.getcandidato_by_id(id=id)
            if self.candidato:
                if senha:
                    self.candidato.senha = HashPassword(senha)
                if email:
                    self.candidato.email = email
                self.candidato.escolaridade = escolaridade
                self.candidato.experiencia = experiencia
                self.candidato.faixa_salarial = faixa_salarial
                self.candidato.save()
                return True
            else:
                return False
        else:
            return False

    def getcandidato_by_id(self, id=None):
        if id:
            self.id = id
            try:
                self.candidato = Candidatos.objects.get(pk=id)
                return self.candidato
            except Candidatos.DoesNotExist:
                return False
        else:
            return False


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

    def get_vaga_by_id(self, id=None):
        if id:
            try:
                self.vaga = Vagas.objects.get(pk=id)
                return self.vaga
            except Vagas.DoesNotExist:
                return False

    def get_candidatos_vaga(self, id=None):
        self.vaga = self.get_vaga_by_id(id=id)
        self.candidatos = self.vaga.candidatos
        return self.candidatos

    def list_vagas(self, empresa=None):
        self.vagas = Vagas.objects.filter(empresa=empresa)
        return self.vagas

    def list_all_vagas(self):
        self.vagas = Vagas.objects.all()
        return self.vagas

    def realizar_candidatura(self, id=None, vaga=None):
        self.vaga = vaga
        if self.vaga:
            self._candidatos = Candidatos()
            self.candidato = self._candidatos.getcandidato_by_id(id=id)
            self.vaga = Candidato_Vaga(
                    vaga=self.vaga, candidato=self.candidato
            )
            self.vaga.save()

    def candidatos_atendem_requisitos(self, vaga=None):
        self.vaga = vaga
        candidatos = Candidato_Vaga.objects.filter(
            vaga=self.vaga,
            candidato__faixa_salarial__range=(
                self.vaga.faixa_salarial_min, self.vaga.faixa_salarial_max
            ),
            candidato__escolaridade=self.vaga.escolaridade,
            candidato__experiencia__gte=self.vaga.experiencia,
            candidato__distancia__lte=self.vaga.distancia_maxima
        ).count()
        return candidatos

    def list_candidatos_atendem_requisitos(self, vaga=None):
        self.vaga = vaga
        candidatos = Candidato_Vaga.objects.filter(
                vaga=self.vaga,
                candidato__faixa_salarial__range=(
                    self.vaga.faixa_salarial_min, self.vaga.faixa_salarial_max
                ),
                candidato__escolaridade=self.vaga.escolaridade,
                candidato__experiencia__gte=self.vaga.experiencia,
                candidato__distancia__lte=self.vaga.distancia_maxima
        )
        return candidatos

    def candidatos_nao_atendem_requisitos(self, vaga=None):
        return Candidato_Vaga.objects.filter(
                vaga=vaga
        ).exclude(
            candidato__faixa_salarial__range=(
                self.vaga.faixa_salarial_min,
                self.vaga.faixa_salarial_max
            ),
            candidato__escolaridade=self.vaga.escolaridade,
            candidato__experiencia__gte=self.vaga.experiencia,
            candidato__distancia__lte=self.vaga.distancia_maxima
        ).count()

    def list_candidato_nao_atendem_requisitos(self, vaga=None):
        return Candidato_Vaga.objects.filter(
            vaga=vaga
        ).exclude(
            candidato__faixa_salarial__range=(
                self.vaga.faixa_salarial_min, self.vaga.faixa_salarial_max
            ),
            candidato__escolaridade=self.vaga.escolaridade,
            candidato__experiencia__gte=self.vaga.experiencia,
            candidato__distancia__lte=self.vaga.distancia_maxima
        )

    def check_candidato(self, id=None, vaga=None):
        if vaga:
            self.vaga = vaga
            self.candidato = id
            try:
                self.candidatura = Candidato_Vaga.objects.get(
                    vaga=self.vaga.id, candidato=self.candidato
                )
                if self.candidatura:
                    return True
                else:
                    return False
            except Candidato_Vaga.DoesNotExist:
                return False
        else:
            return False

    def get_candidatosvaga_by_id(self, id=None):
        if id:
            self.id = id
            try:
                self.candidato_vaga = Candidato_Vaga.objects.get(pk=self.id)
                if self.candidato_vaga:
                    return self.candidato_vaga
                else:
                    return False
            except Candidato_Vaga.DoesNotExist:
                return False
        else:
            return False


class Candidato_Vaga(models.Model):
    candidato = models.ForeignKey(Candidatos, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vagas, on_delete=models.CASCADE)
