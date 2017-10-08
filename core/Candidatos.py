# -*- coding: utf-8 -*-
import hashlib
from json import dump, dumps
from models import Candidatos


def HashPassword(senha=None):
    if senha:
        senha = hashlib.sha512(u'{}'.format(senha)).hexdigest()
        return senha
    else:
        return False


def Login(request, email=None, senha=None):
    if not request.session.get('email', False):
        try:
            login_candidato = Candidatos.objects.get(
                email=email, senha=HashPassword(senha)
            )

            if request.session.get('email_empresa', False):
                del request.session['email_empresa']
            if request.session.get('id_empresa', False):
                del request.session['id_empresa']
            if request.session.get('empresa', False):
                del request.session['empresa']

            request.session['email'] = login_candidato.email
            request.session['id'] = login_candidato.id
            request.session['candidato'] = True
            return login_candidato
        except Candidatos.DoesNotExist:
            return False
    else:
        return True


def CheckLogin(request):
    email_candidato = request.session.get('email', False)
    email_empresa = request.session.get('email_empresa', False)

    if email_candidato or email_empresa:
        return True
    else:
        return False


def CandidatoUpdate(id=None, email=None, escolaridade=None,
                    experiencia=None, distancia=None,
                    faixa_salarial=None, senha=None):
    if id:
        distancia = distancia.replace(',', '.')
        faixa_salarial = faixa_salarial.replace(',', '.')
        candidato = GetCandidatoById(id=id)
        if candidato:
            if senha:
                candidato.senha = HashPassword(senha)
            if email:
                candidato.email = email
            candidato.escolaridade = escolaridade
            candidato.experiencia = experiencia
            candidato.distancia = distancia
            candidato.faixa_salarial = faixa_salarial
            candidato.save()
            return True
        else:
            return False
    else:
        return False


def GetCandidatoById(id=None):
    if id:
        try:
            candidato = Candidatos.objects.get(pk=id)
            return candidato
        except Candidatos.DoesNotExist:
            return False
