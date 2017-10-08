# -*- coding: utf-8 -*-

from models import Vagas, Candidato_Vaga, Candidatos
from django.db.models import Q
from Candidatos import GetCandidatoById


def ListVagas(empresa=None):
    vagas = Vagas.objects.filter(empresa=empresa)
    return vagas


def GetVagaById(id=None):
    if id:
        try:
            vaga = Vagas.objects.get(pk=id)
            return vaga
        except Vagas.DoesNotExist:
            return False
    else:
        return False


def GetCandidatosVaga(id=None):
    vaga = GetVagaById(id=id)
    candidatos = vaga.candidatos
    return candidatos


def ListAllVagas():
    vagas = Vagas.objects.all()
    return vagas


def RealizarCandidatura(id=None, vaga=None):
    if vaga:
        candidato = GetCandidatoById(id=id)
        vaga = Candidato_Vaga(vaga=vaga, candidato=candidato)
        vaga.save()


def CandidatosAtendemRequisitos(vaga=None):
    candidatos = Candidato_Vaga.objects.filter(
            vaga=vaga,
            candidato__faixa_salarial__range=(
                vaga.faixa_salarial_min, vaga.faixa_salarial_max
            ),
            candidato__escolaridade=vaga.escolaridade,
            candidato__experiencia__gte=vaga.experiencia,
            candidato__distancia__lte=vaga.distancia_maxima
    ).count()
    return candidatos


def ListCandidatosAtendemRequisitos(vaga=None):
    candidatos = Candidato_Vaga.objects.filter(
            vaga=vaga,
            candidato__faixa_salarial__range=(
                vaga.faixa_salarial_min, vaga.faixa_salarial_max
            ),
            candidato__escolaridade=vaga.escolaridade,
            candidato__experiencia__gte=vaga.experiencia,
            candidato__distancia__lte=vaga.distancia_maxima
    )
    return candidatos


def CandidatosNaoAtendemRequisitos(vaga=None):
    candidatos = Candidato_Vaga.objects.filter(vaga=vaga).exclude(
            candidato__faixa_salarial__range=(
                    vaga.faixa_salarial_min, vaga.faixa_salarial_max
            ),
            candidato__escolaridade=vaga.escolaridade,
            candidato__experiencia__gte=vaga.experiencia,
            candidato__distancia__lte=vaga.distancia_maxima
    ).count()
    return candidatos


def ListCandidatosNaoAtendemRequisitos(vaga=None):
    candidatos = Candidato_Vaga.objects.filter(vaga=vaga).exclude(
            candidato__faixa_salarial__range=(
                    vaga.faixa_salarial_min, vaga.faixa_salarial_max
            ),
            candidato__escolaridade=vaga.escolaridade,
            candidato__experiencia__gte=vaga.experiencia,
            candidato__distancia__lte=vaga.distancia_maxima
    )
    return candidatos


def CheckCandidato(id=None, vaga=None):
    if vaga:
        try:
            candidatura = Candidato_Vaga.objects.get(
                    vaga=vaga.id, candidato=id
            )
            if candidatura:
                return True
            else:
                return False
        except Candidato_Vaga.DoesNotExist:
            return False
    else:
        return False


def GetCandidatosVagaById(id=None):
    if id:
        print(id)
        try:
            candidato_vaga = Candidato_Vaga.objects.get(pk=id)
            if candidato_vaga:
                return candidato_vaga
            else:
                return False
        except Candidato_Vaga.DoesNotExist:
            return False
    else:
        return False
