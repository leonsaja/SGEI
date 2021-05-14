from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import  ListView
from django.core.files.storage import FileSystemStorage
from .forms import EditalForm, PerguntaForm, AlternativaForm, IncricaoFormAv
from .models import Edital, Inscricao, Pergunta, Alternativa, Resposta
from django.core.paginator import Paginator
from django.db.models import Q,Value
from django.db.models.functions import Concat
from django.contrib import  messages
#Edital área

# administração

@login_required
def edital_list_adm(request):
    context = {}
    editais_abertos = Edital.objects.filter(status='ab')
    editais_analise = Edital.objects.filter(status='em')
    editais_fechados = Edital.objects.filter(status='fn')


    context['editais_abertos'] = editais_abertos
    context['editais_analise'] = editais_analise
    context['editais_fechados'] = editais_fechados


    return render(request,'edital/list_edital.html', context)

@login_required
def edital_view_adm(request, id):
    context = {}
    edital= get_object_or_404(Edital, pk=id)
    perguntas = edital.pergunta_set.all()
    context['edital'] = edital
    context['perguntas'] = perguntas
    return render(request,'edital/view_edital.html',context)

@login_required
def edital_add(request):
    edital = Edital()
    context = {}

    if request.method == 'POST':
        form = EditalForm(request.POST or None, request.FILES or None, instance=edital, prefix='edital')

        if form.is_valid():
            form = form.save(commit=False)
            edital = form.save()
            messages.add_message(request, messages.SUCCESS, 'Edital realizado com sucesso !')
            return redirect('editais:edital_list')
        else:
            context['form'] = EditalForm(request.POST or None, request.FILES or None, instance=edital, prefix='edital')


    else:
        context['form'] = EditalForm( instance=edital, prefix='edital')



    return render(request,'edital/add_edital.html', context)


@login_required
def  edital_edit(request, id):
    context = {}
    edital = get_object_or_404(Edital, pk=id)

    if request.method == 'POST':
        form = EditalForm(request.POST or None, request.FILES or None, instance=edital, prefix='edital')

        if form.is_valid():
            form = form.save(commit=False)
            form.save()


            return redirect('editais:edital_view', id=edital.id)
        else:
            context['form'] = EditalForm(request.POST or None, request.FILES or None, instance=edital, prefix='edital')


    else:
        context['form'] = EditalForm(instance=edital, prefix='edital')



    return render(request,'edital/edit_edital.html', context)


@login_required
def edital_delete(request, id):
    edital = get_object_or_404(Edital, pk=id)
    edital.delete()

    return redirect('editais:edital_list')


###Alunos
class EditalList(ListView):
    template_name = 'edital/list_edital_inscri.html'
    model = Edital


def edital_list_aluno(request):
    context = {}
    editais_abertos = Edital.objects.filter(status='ab')
    editais_analise = Edital.objects.filter(status='em')
    editais_fechados = Edital.objects.filter(status='fn')

    context['editais_abertos'] = editais_abertos
    context['editais_analise'] = editais_analise
    context['editais_fechados'] = editais_fechados

    return render(request, 'edital/list_edital_inscri.html', context)


def edital_view(request, id):
    context = {}
    edital= get_object_or_404(Edital, pk=id)
    request.user
    if request.user.is_anonymous == False:
        user = request.user
        inscricao = Inscricao.objects.filter(user=user,edital=edital)
        context['situacao'] = False

        if inscricao:
            context['situacao'] = True

    context['edital'] = edital
    return render(request,'edital/view_edital_inscri.html',context)



def resultado_edital(request,id):
    context = {}
    edital = get_object_or_404(Edital, pk=id)
    aprovados = Inscricao.objects.filter(edital=edital, status='df')
    reprovados = Inscricao.objects.filter(edital=edital, status='in')


    context['edital'] = edital
    context['aprovados'] = aprovados
    context['reprovados'] = reprovados
    return render(request,'edital/resultado_edital.html',context)


#------------------- Perguntas ---------------------
@login_required
def pergunta_add(request, id_edital):
    form_alternativa_factory = inlineformset_factory(Pergunta, Alternativa, form=AlternativaForm)

    edital = get_object_or_404(Edital, pk=id_edital)
    pergunta = Pergunta()
    pergunta.edital = edital
    context = {}

    if request.method == 'POST':

        form = PerguntaForm(request.POST or None, request.FILES or None, instance=pergunta, prefix='pergunta')
        alternativa_form = form_alternativa_factory(request.POST or None, request.FILES or None, instance=pergunta,
                                                    prefix='alternativa')


        if form.is_valid() and alternativa_form.is_valid():
            form = form.save(commit=False)
            form.save()
            alternativa_form.save()
            return redirect('editais:edital_view',id =edital.id)
        else:
            context['edital'] = edital
            context['form'] = PerguntaForm(request.POST or None, request.FILES or None, instance=pergunta,
                                           prefix='pergunta')
            context['form_alternativa'] = form_alternativa_factory(request.POST or None, request.FILES or None,
                                                                   instance=pergunta, prefix='alternativa')

    else:
        context['edital'] = edital
        context['form'] = PerguntaForm(instance=pergunta, prefix='pergunta')
        context['form_alternativa'] = form_alternativa_factory(instance=pergunta, prefix='alternativa')

    return render(request, 'pergunta/add_pergunta.html', context)

@login_required
def pergunta_edit(request, id):
    form_alternativa_factory = inlineformset_factory(Pergunta, Alternativa, form=AlternativaForm)
    pergunta = get_object_or_404(Pergunta, pk=id)
    edital = pergunta.edital

    context = {}

    if request.method == 'POST':

        form = PerguntaForm(request.POST or None, request.FILES or None, instance=pergunta, prefix='pergunta')
        alternativa_form = form_alternativa_factory(request.POST or None, request.FILES or None, instance=pergunta,
                                                    prefix='alternativa')


        if form.is_valid() and alternativa_form.is_valid():
            form = form.save(commit=False)
            form.save()
            alternativa_form.save()
            return redirect('editais:edital_view',id =edital.id)
        else:
            context['edital'] = edital
            context['form'] = PerguntaForm(request.POST or None, request.FILES or None, instance=pergunta,
                                           prefix='pergunta')
            context['form_alternativa'] = form_alternativa_factory(request.POST or None, request.FILES or None,
                                                                   instance=pergunta, prefix='alternativa')

    else:
        context['edital'] = edital
        context['form'] = PerguntaForm(instance=pergunta, prefix='pergunta')
        context['form_alternativa'] = form_alternativa_factory(instance=pergunta, prefix='alternativa')

    return render(request, 'pergunta/edit_pergunta.html', context)

@login_required
def pergunta_delete(request, id):
    pergunta = get_object_or_404(Pergunta, pk=id)
    edital = pergunta.edital
    pergunta.delete()

    return redirect('editais:edital_view',id =edital.id)


@login_required
def inscricao_list(request):

    context = {}
    editais = Edital.objects.all()

    search = request.GET.get('busca')
    campos = Concat('user__first_name', Value(' '), 'user__last_name') # user__first_name relacionamento ForeignKey

    if not search:
        search = ""

    status = request.GET.get('status')
    id_edital = request.GET.get('edital')

    if id_edital:
        edital = get_object_or_404(Edital, pk=id_edital)

        if status:
            inscricao_list = Inscricao.objects.filter(status=status, edital=edital)

        else:
            inscricao_list = Inscricao.objects.filter(edital=edital)

    else:
        if status:
            inscricao_list = Inscricao.objects.filter(status=status)

        else:
            inscricao_list = Inscricao.objects.annotate(nome_completo=campos).filter(Q(nome_completo__icontains=search) | Q(user__fone=search))

    paginator = Paginator(inscricao_list,20)
    page = request.GET.get('p')
    inscricao_list = paginator.get_page(page)



    context['inscricao_list'] = inscricao_list
    context['editais'] = editais

    return render(request, 'inscricao/list_inscricao.html', context)


@login_required
def inscricao_list_user(request):
    context ={}
    incricoes = Inscricao.objects.filter(user=request.user)

    context['incricoes'] = incricoes

    return render(request, 'inscricao/user_list_inscricoes.html',context)

@login_required
def inscricao_view(request, id):
    context = {}
    inscricao= get_object_or_404(Inscricao, pk=id)

    if request.method == 'POST':
        form = IncricaoFormAv(request.POST or None, instance=inscricao)

        if form.is_valid():
            form.save()
            return redirect('editais:inscricao_list')

    else:
        form = IncricaoFormAv(request.POST or None, instance=inscricao)

    context['inscricao'] = inscricao
    context['form'] = form

    return render(request,'inscricao/view_inscricao.html',context)

@login_required
def inscricao_view_user(request, id):
    context = {}
    inscricao= get_object_or_404(Inscricao, pk=id)

    context['inscricao'] = inscricao

    return render(request, 'inscricao/view_inscricao_user.html',context)


@login_required
def inscricao_do(request,id_edital):

    context = {}
    edital = get_object_or_404(Edital, pk=id_edital)
    context['edital'] = edital
    inscricao = Inscricao()
    inscricao.edital = edital
    inscricao.user = request.user


    if(request.method == 'POST'):
        fs = FileSystemStorage()
        inscricao.save()

        for pergunta in edital.pergunta_set.all():
            resp = Resposta(inscricao=inscricao, pergunta=pergunta)

            if pergunta.is_aberta and pergunta.has_arquivo:
                nome_arq = 'arquivo-' + str(pergunta.id)
                arq = request.FILES.get(nome_arq)
                nome_save = 'inscricoes/' + arq.name
                resp.arquivo = fs.save(nome_save, arq)

            elif pergunta.is_aberta:
                aux = request.POST.get('pergunta-' + str(pergunta.id))
                resp.resposta_aberta = aux
            else:
                aux = request.POST.get('pergunta-' + str(pergunta.id))
                alt = Alternativa.objects.get(id=int(aux))
                resp.alternativa = alt

            resp.save()

        return redirect('editais:inscricao_list_user')
    return render(request, 'inscricao/do_inscricao.html', context)

@login_required
def inscricao_edit(request, id):
    inscricao = get_object_or_404(Inscricao, pk=id)
    context={}
    resposta=Resposta()
    resposta.inscricao=inscricao


    if request.method == "POST":
        fs = FileSystemStorage()

        for resp in inscricao.resposta_set.all():

            if resp.pergunta.is_aberta and resp.pergunta.has_arquivo:
                nome_arq = 'arquivo-' + str(resp.pergunta.id)
                arq = request.FILES.get(nome_arq, None)
                if arq:
                    nome_save = 'inscricoes/' + arq.name
                    resp.arquivo = fs.save(nome_save, arq)


            elif resp.pergunta.is_aberta:
                aux = request.POST.get('pergunta-' + str(resp.pergunta.id))
                resp.resposta_aberta = aux
            else:
                aux = request.POST.get('pergunta-' + str(resp.pergunta.id))
                alt = Alternativa.objects.get(id=int(aux))
                resp.alternativa = alt

            resp.save()
        """
            aux = request.POST.get('pergunta-' + str(resp.pergunta.id))
            if resp.pergunta.is_aberta:
                resp.resposta_aberta = aux
            elif resp.pergunta.has_arquivo:
                nome_arq = 'arquivo-' + str(resp.pergunta.id)
                arq = request.FILES.get(nome_arq,None)
                if arq:

                    nome_save = 'inscricoes/' + arq.name
                    resp.arquivo = fs.save(nome_save, arq)

            else:
                alt = Alternativa.objects.get(id=int(aux))
                resp.alternativa = alt

            resp.save()
            """
        return redirect('editais:inscricao_list_user')
    else:
        context['inscricao'] = inscricao
    return render(request, 'inscricao/edit_inscricao.html', context)