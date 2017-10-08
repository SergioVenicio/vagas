# -*- coding: utf-8 -*-
from models import Empresas
from Candidatos import HashPassword


def LoginEmpresa(request, email=None, senha=None):
    if not request.session.get('email_empresa', False):
        try:
            login_empresa = Empresas.objects.get(
                email=email, senha=HashPassword(senha)
            )

            if request.session.get('email', False):
                del request.session['email']
            if request.session.get('id', False):
                del request.session['id']
            if request.session.get('candidato'):
                del request.session['candidato']

            request.session['email_empresa'] = login_empresa.email
            request.session['id_empresa'] = login_empresa.id
            request.session['empresa'] = True
            return login_empresa
        except Empresas.DoesNotExist:
            return False
    else:
        return True


def EmpresaUpdate(id=None, email=None, razao_social=None, endereco=None,
                  ramo=None, numero=None, senha=None):
    if id:
        empresa = GetEmpresaById(id=id)
        if empresa:
            if senha:
                empresa.senha = HashPassword(senha)
            empresa.email = email
            empresa.razao_social = razao_social
            empresa.endereco = endereco
            empresa.ramo = ramo
            empresa.numero = numero
            empresa.save()
            return True
        else:
            return False
    else:
        return False


def GetEmpresaById(id=id):
    try:
        empresa = Empresas.objects.get(pk=id)
        return empresa
    except Empresas.DoesNotExist:
        return False
