# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from models import ESCOLARIDADE_CHOICES
from django.views.decorators.csrf import csrf_exempt
from forms import CandidatoForm, EditarCandidatoForm, EmpresaForm, \
                  EmpresaLoginForm, EmpresaEditForm, VagaEmpresa, \
                  EmpresaEditarCandidatoForm
from Candidatos import Login, CheckLogin, GetCandidatoById, CandidatoUpdate, \
                       HashPassword
from Empresas import LoginEmpresa, EmpresaUpdate, GetEmpresaById
from Vagas import ListVagas, GetVagaById, ListAllVagas, \
                  RealizarCandidatura, CandidatosAtendemRequisitos, \
                  CheckCandidato, CandidatosNaoAtendemRequisitos, \
                  ListCandidatosAtendemRequisitos, \
                  ListCandidatosNaoAtendemRequisitos, GetCandidatosVagaById
from json import dumps


def Add_candidato(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST)
        if form.is_valid():
            candidato = form.save(commit=False)
            candidato.senha = HashPassword(candidato.senha)
            candidato.save()
            request.session['email'] = candidato.email
            request.session['id'] = candidato.id
            request.session['candidato'] = True
            return HttpResponseRedirect(reverse('core:Home'))
        else:
            context = {'form': CandidatoForm, 'error': True}
            return render(request, 'add_candidato.html', context)

    context = {'form': CandidatoForm}
    return render(request, 'add_candidato.html', context)


def Login_candidato(request):
    if request.method == 'POST':
        email = request.POST.get('email', False)
        senha = request.POST.get('senha', False)
        if Login(request=request, email=email, senha=senha):
            return HttpResponseRedirect(reverse('core:Home'))
        else:
            context = {'form': CandidatoForm, 'error': True}
            return render(request, 'login_candidato.html', context)

    context = {'form': CandidatoForm}
    return render(request, 'login_candidato.html', context)


def Logout(request):
    id = request.session.get('id', False)
    email = request.session.get('email', False)
    candidato = request.session.get('candidato', False)
    if id and email and candidato:
        del request.session['email']
        del request.session['candidato']
        del request.session['id']

    return HttpResponseRedirect(reverse('core:Login_candidato'))


@csrf_exempt
def Editar_candidato(request):
    if CheckLogin(request):
        id = request.session.get('id', False)
        if request.method == 'POST':
            if id:
                email = request.POST.get('email', False)
                escolaridade = request.POST.get('escolaridade', False)
                experiencia = request.POST.get('experiencia', False)
                distancia = request.POST.get('distancia', False)
                faixa_salarial = request.POST.get('faixa_salarial', False)
                senha = request.POST.get('senha', False)
                candidato = CandidatoUpdate(
                        id=id, email=email, escolaridade=escolaridade,
                        experiencia=experiencia, distancia=distancia,
                        faixa_salarial=faixa_salarial, senha=senha
                )
                return HttpResponse(dumps(candidato),
                                    content_type="application/json")
            else:
                return HttpResponse(dumps('false'),
                                    content_type="application/json")

        candidato = GetCandidatoById(id=id)
        context = {'form': EditarCandidatoForm(instance=candidato)}
        return render(request, 'editar_candidato.html', context)
    else:
        return HttpResponseRedirect(reverse('core:Login_candidato'))


def Add_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            empresa = form.save(commit=False)
            empresa.senha = HashPassword(empresa.senha)
            empresa.save()
            request.session['email_empresa'] = empresa.email
            request.session['id_empresa'] = empresa.id
            request.session['empresa'] = True
            return HttpResponseRedirect(reverse('core:Home'))
    context = {'form': EmpresaForm}
    return render(request, 'add_empresa.html', context)


def Login_empresa(request):
    if request.method == 'POST':
        email = request.POST.get('email', False)
        senha = request.POST.get('senha', False)
        if LoginEmpresa(request, email=email, senha=senha):
            return HttpResponseRedirect(reverse('core:Home'))
        else:
            context = {'form': EmpresaLoginForm, 'error': True}
            return render(request, 'login_empresa.html', context)

    context = {'form': EmpresaLoginForm}
    return render(request, 'login_empresa.html', context)


def LogoutEmpresa(request):
    id = request.session.get('id_empresa', False)
    email = request.session.get('email_empresa', False)
    empresa = request.session.get('empresa', False)
    if id and email and empresa:
        del request.session['id_empresa']
        del request.session['email_empresa']
        del request.session['empresa']

    return HttpResponseRedirect(reverse('core:Login_empresa'))


@csrf_exempt
def Editar_empresa(request):
    if CheckLogin(request):
        id = request.session.get('id_empresa', False)
        if request.method == 'POST':
            if id:
                email = request.POST.get('email', False)
                razao_social = request.POST.get('razao_social', False)
                endereco = request.POST.get('endereco', False)
                ramo = request.POST.get('ramo', False)
                numero = request.POST.get('numero', False)
                senha = request.POST.get('senha', False)
                empresa = EmpresaUpdate(
                            id=id, email=email, razao_social=razao_social,
                            endereco=endereco, ramo=ramo, numero=numero,
                            senha=senha
                          )
                return HttpResponse(dumps(empresa),
                                    content_type="application/json")
            else:
                return HttpResponse(dumps('false'),
                                    content_type="application/json")

        context = {'form': EmpresaEditForm(instance=GetEmpresaById(id=id))}
        return render(request, 'editar_empresa.html', context)
    else:
        return HttpResponseRedirect(reverse('core:Login_empresa'))


def CadastrarVagaEmpresa(request):
    if request.method == 'POST':
        id = request.session.get('id_empresa', False)
        empresa = GetEmpresaById(id=id)
        form = VagaEmpresa(request.POST)
        if form.is_valid():
            vagaempresa = form.save(commit=False)
            vagaempresa.empresa = empresa
            vagaempresa.save()
            context = {'form': VagaEmpresa, 'vaga': True}
            return render(request, 'cadastrarvagaempresa.html', context)
        else:
            context = {'form': form}
            return render(request, 'cadastrarvagaempresa.html', context)
    context = {'form': VagaEmpresa}
    return render(request, 'cadastrarvagaempresa.html', context)


@csrf_exempt
def ExcluirVagaEmpresa(request):
    if CheckLogin(request):
        id = request.POST.get('id', False)
        vaga = GetVagaById(id=id)
        if vaga:
            vaga.delete()
            return HttpResponse(dumps(True),
                                content_type="application/json")
        else:
            return HttpResponse(dumps(False),
                                content_type="application/json")
    else:
        return HttpResponseRedirect(reverse('core:Login_empresa'))


@csrf_exempt
def EmpresaEditarVaga(request, id=None):
    if CheckLogin(request):
        if request.session.get('email_empresa', False):
            if request.method == 'POST':
                id = request.POST.get('id', False)
                vaga = GetVagaById(id=id)
                if vaga:
                    empresa = GetEmpresaById(
                            id=request.session.get('id_empresa')
                    )
                    descricao = request.POST.get('descricao', False)
                    faixa_min = request.POST.get('faixa_salarial_min', False)
                    faixa_max = request.POST.get('faixa_salarial_max', False)
                    experiencia = request.POST.get('experiencia', False)
                    escolaridade = request.POST.get('escolaridade', False)
                    distancia = request.POST.get('distancia', False)
                    faixa_min = faixa_min.replace('.', '').replace(',', '.')
                    faixa_max = faixa_max.replace('.', '').replace(',', '.')
                    distancia = distancia.replace('.', '').replace(',', '.')
                    vaga.empresa = empresa
                    vaga.descricao = descricao
                    vaga.faixa_salarial_min = faixa_min
                    vaga.faixa_salarial_max = faixa_max
                    vaga.experiencia = experiencia
                    vaga.escolaridade = escolaridade
                    vaga.distancia_maxima = distancia
                    vaga.save()
                    return HttpResponse(dumps({'return': True}),
                                        content_type="application/json")
                else:
                    return HttpResponse(dumps({'return': False}),
                                        content_type="application/json")
            vaga = GetVagaById(id=id)
            form = VagaEmpresa(instance=vaga)
            context = {'form': form, 'vaga_id': vaga.id}
            return render(request, 'editvagaempresa.html', context)
        else:
            return HttpResponseRedirect(reverse('core:Login_empresa'))
    else:
        return HttpResponseRedirect(reverse('core:Login_empresa'))


def VagasCandidatos(request, id=None):
    if CheckLogin(request):
        if request.session.get('email_empresa', False):
            vaga = GetVagaById(id=id)
            candidatos_atendem = CandidatosAtendemRequisitos(vaga=vaga)
            candidatos_nao_atendem = CandidatosNaoAtendemRequisitos(vaga=vaga)
            list_candidatos_atendem = ListCandidatosAtendemRequisitos(
                                                                    vaga=vaga)
            list_candidatos_nao_atendem = ListCandidatosNaoAtendemRequisitos(
                                                                    vaga=vaga)
            context = {
                'vaga': vaga, 'candidatos': candidatos_atendem,
                'candidatos_nao_atendem': candidatos_nao_atendem,
                'list_atendem': list_candidatos_atendem,
                'list__nao_atendem': list_candidatos_nao_atendem,
                'escolaridades': ESCOLARIDADE_CHOICES
            }
            return render(request, 'vagas_candidatos.html', context)
        else:
            return HttpResponseRedirect(reverse('core:Home'))
    else:
        return HttpResponseRedirect(reverse('core:Login_empresa'))


@csrf_exempt
def Candidatar(request, id=None):
    vaga = GetVagaById(id=id)
    if request.method == 'POST':
        id_candidato = request.POST.get('id')
        resposta = RealizarCandidatura(id=id_candidato, vaga=vaga)
        return HttpResponse(dumps({'return': resposta}),
                            content_type="application/json")
    candidatura = CheckCandidato(id=request.session.get('id'), vaga=vaga)
    context = {
            'vaga': vaga, 'candidatura': candidatura,
            'escolaridades': ESCOLARIDADE_CHOICES
    }
    return render(request, 'candidatar.html', context)


@csrf_exempt
def EmpresaEditarCandidato(request, id_candidato=None):
    candidato = GetCandidatoById(id=id_candidato)
    if request.method == 'POST':
        escolaridade = request.POST.get('escolaridade', False)
        experiencia = request.POST.get('experiencia', False)
        print(experiencia)
        distancia = request.POST.get('distancia', False)
        faixa_salarial = request.POST.get('faixa_salarial', False)
        candidato = CandidatoUpdate(
                id=id_candidato, escolaridade=escolaridade,
                experiencia=experiencia, distancia=distancia,
                faixa_salarial=faixa_salarial
        )
        return HttpResponse(dumps({'return': True}),
                            content_type="application/json")
    form = EmpresaEditarCandidatoForm(instance=candidato)
    context = {'form': form, 'candidato': candidato}
    return render(request, 'empresaeditarcandidato.html', context)


@csrf_exempt
def EmpresaDeletarVaga(request):
    if request.method == 'POST':
        id = request.POST.get('id', False)
        if id:
            candidato_vaga = GetCandidatosVagaById(id=id)
            print(candidato_vaga)
            if candidato_vaga:
                candidato_vaga.delete()
                return HttpResponse(dumps(True),
                                    content_type="application/json")
            else:
                return HttpResponse(dumps(False),
                                    content_type="application/json")
        else:
            return HttpResponse(dumps(False),
                                content_type="application/json")
    return HttpResponse('ok')


def Home(request):
    if CheckLogin(request):
        if request.session.get('email_empresa', False):
            empresa = GetEmpresaById(request.session.get('id_empresa'))
            vagas = ListVagas(empresa=empresa)
            context = {
                    'vagas': vagas,
                    'escolaridades': ESCOLARIDADE_CHOICES
            }
            return render(request, 'home.html', context)
        elif request.session.get('email', False):
            context = {
                    'vagas': ListAllVagas(),
                    'escolaridades': ESCOLARIDADE_CHOICES
                }
            return render(request, 'home.html', context)
        return render(request, 'home.html')
    else:
        return HttpResponseRedirect(reverse('core:Login_candidato'))
