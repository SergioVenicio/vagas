# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Add_candidato, name="Add_candidato"),
    url(r'^candidato/login/$', views.Login_candidato, name="Login_candidato"),
    url(r'^candidato/logout/$', views.Logout, name="Logout"),
    url(r'^candidato/editar/$',
        views.Editar_candidato, name="Editar_candidato"),
    url(r'^candidato/(?P<id>[0-9]+)/$', views.Candidatar, name="Candidatar"),
    url(r'^empresa/cadastrar/$', views.Add_empresa, name="Add_empresa"),
    url(r'^empresa/editar/$', views.Editar_empresa, name="Editar_empresa"),
    url(r'^empresa/login/$', views.Login_empresa, name="Login_empresa"),
    url(r'^empresa/logout/$', views.LogoutEmpresa, name="Logout_empresa"),
    url(r'^empresa/vaga/cadastrar/$', views.CadastrarVagaEmpresa,
        name="CadastrarVagaEmpresa"),
    url(r'^empresa/vaga/(?P<id>[0-9]+)/$', views.VagasCandidatos,
        name="VagasCandidatos"),
    url(r'^empresa/vaga/(?P<id>[0-9]+)/editar/$', views.EmpresaEditarVaga,
        name='EmpresaEditarVaga'),
    url(r'^empresa/vaga/excluir/$', views.ExcluirVagaEmpresa,
        name="ExcluirVagaEmpresa"),
    url(r'^empresa/editar/candidato/(?P<id_candidato>[0-9]+)/$',
        views.EmpresaEditarCandidato, name="EmpresaEditarCandidato"),
    url(r'^empresa/deletar/vaga_candidato/$',
        views.EmpresaDeletarVaga, name="EmpresaDeletarVaga"),
    url(r'^home/$', views.Home, name="Home")
]
