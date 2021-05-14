from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.shortcuts import render, redirect
# from editais.models import Edital
from django.contrib.auth.decorators import login_required
from editais.models import Edital, Inscricao
from django.contrib import messages


# from editais.models import Inscricao, Edital

def home(request):
    context = {}

    editais_abertos = Edital.objects.filter(status='ab')
    editais_analise = Edital.objects.filter(status='em')
    editais_fechados = Edital.objects.filter(status='fn')

    context['editais_abertos'] = editais_abertos
    context['editais_analise'] = editais_analise
    context['editais_fechados'] = editais_fechados

    return render(request, 'home.html', context)


def mylogout(request):
    logout(request)
    return redirect('core:home')


@login_required
def index(request):
    context = {}
    editais_abertos = Edital.objects.filter(status='ab')
    editais_analise = Edital.objects.filter(status='em')
    editais_fechados = Edital.objects.filter(status='fn')
    inscricao_analise = Inscricao.objects.filter(status="an")

    context['qtd_inscricao_analise'] = inscricao_analise.count()
    context['qtd_editais_abertos'] = editais_abertos.count()
    context['qtd_editais_analise'] = editais_analise.count()
    context['qtd_editais_fechados'] = editais_fechados.count()

    return render(request, 'index.html', context)