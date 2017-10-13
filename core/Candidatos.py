# -*- coding: utf-8 -*-
import hashlib
from models import Candidatos


def HashPassword(senha=None):
    if senha:
        senha = hashlib.sha512(u'{}'.format(senha)).hexdigest()
        return senha
    else:
        return False


def CheckLogin(request):
    email_candidato = request.session.get('email', False)
    email_empresa = request.session.get('email_empresa', False)

    if email_candidato or email_empresa:
        return True
    else:
        return False


class _Candidatos():
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
