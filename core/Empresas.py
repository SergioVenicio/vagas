# -*- coding: utf-8 -*-
from models import Empresas
from Candidatos import HashPassword


class _Empresas():
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
