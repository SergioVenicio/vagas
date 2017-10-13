# -*- coding: utf-8 -*-

from models import Vagas, Candidato_Vaga
from Candidatos import _Candidatos


class _Vagas():
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
            self._candidatos = _Candidatos()
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
        self.vaga = vaga
        self.candidatos = Candidato_Vaga.objects.filter(
                vaga=self.vaga
        ).exclude(
            candidato__faixa_salarial__range=(
                self.vaga.faixa_salarial_min,
                self.vaga.faixa_salarial_max
            ),
            candidato__escolaridade=self.vaga.escolaridade,
            candidato__experiencia__gte=self.vaga.experiencia,
            candidato__distancia__lte=self.vaga.distancia_maxima
        ).count()
        return self.candidatos

    def list_candidato_nao_atendem_requisitos(self, vaga=None):
        self.vaga = vaga
        self.candidatos = Candidato_Vaga.objects.filter(
            vaga=self.vaga
        ).exclude(
            candidato__faixa_salarial__range=(
                self.vaga.faixa_salarial_min, self.vaga.faixa_salarial_max
            ),
            candidato__escolaridade=self.vaga.escolaridade,
            candidato__experiencia__gte=self.vaga.experiencia,
            candidato__distancia__lte=self.vaga.distancia_maxima
        )
        return self.candidatos

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
