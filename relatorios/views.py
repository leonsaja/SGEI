from django.shortcuts import render, get_object_or_404, redirect
from editais.models import Edital, Inscricao
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

def relatorioedital(request, id):

    edital = get_object_or_404(Edital, pk=id)


    template_path = 'relatorio/inscricoes/inscricoes_edital.html'
    context = {'edital':edital}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download:
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #if display:
    response['Content-Disposition'] ='filename="Lista de Candidatos Inscrito no edital.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def pdf_inscricaoDetelhada(request, id):

    inscricao = get_object_or_404(Inscricao, pk=id)

    template_path = 'relatorio/aluno/aluno_inscri.html'
    context = {'inscricao': inscricao}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download:
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display:
    response['Content-Disposition'] = 'filename="Inscrição do Aluno.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

