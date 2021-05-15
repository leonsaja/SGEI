from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUsuarioCreateForm, LoginForm, CustomUsuarioChangeForm, UserAdminForm
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib.auth import  update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

def login_view(request):

    form = LoginForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("Login")
            password = form.cleaned_data.get("Senha")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Seja Bem-Vindo !')
                return redirect('core:index')
            else:
                messages.add_message(request, messages.ERROR, 'Email ou senha invalida')

        else:
            messages.add_message(request, messages.ERROR, 'Erro ao carregar o formulario ')

    return render(request, "account/login.html", {"form": form})

def register_user(request):

    if request.method == "POST":
        form = CustomUsuarioCreateForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cadastro realizado com sucesso !')
            return redirect('accounts:login')
        else:
            messages.add_message(request, messages.ERROR, 'Por favor, preenchar os campos corretamente !!!')
    else:
        form = CustomUsuarioCreateForm()
    return render(request, "account/register.html", {"form": form})


def usuario_edit(request, id):
    context = {}
    u=id
    user = get_object_or_404(User, pk=id)


    print(u)
    if request.method == 'POST':

        form = CustomUsuarioChangeForm(request.POST, request.FILES, instance=user, prefix='user')

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Perfil Atualizado com sucesso ')

            return redirect('accounts:upd_user', id=user.id)
        else:
            context['usuario'] = user
            context['form'] = CustomUsuarioChangeForm(request.POST or None, instance=user, prefix='user')

    else:
        context['form'] = CustomUsuarioChangeForm(instance=user, prefix='user')
        context['usuario'] = user


    return render(request, 'user/edit_user.html', context)


def perfil(request):
    context = {}
    user = request.user

    context['user'] = user
    return render(request, 'user/edit_user.html', context)

def edit_password(request):

    context = {}
    user = request.user
    form = PasswordChangeForm(request.POST or None)
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.add_message(request, messages.SUCCESS, 'Senha altera com sucesso  !!')
            return redirect('accounts:upd_user', id=user.id)

    else:
        form = PasswordChangeForm(request.POST or None)

    context['form'] = form
    return render(request, 'user/edit_password.html', context)

def user_novo(request):
    context ={}
    request.user

    user = User()
    form = UserAdminForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        form = UserAdminForm(request.POST, request.FILES)
        print('teste')
        if form.is_valid():
            print('teste')
            form = form.save(commit=False)
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cadastro realizado com sucesso !!')
            return redirect('accounts:list_user')
    else:
        form = UserAdminForm(request.POST or None, request.FILES or None)

    context['form'] = form
    return render(request, 'user/add_user.html', context)

"""
def create_user_arquivo(request):
    context = {}
    fs = FileSystemStorage()

    if (request.method == 'POST'):

        arq = request.FILES['arquivo']

        fs.save('accounts/' + arq.name, arq)

        caminho = 'media/accounts/' + arq.name

        dados = open(caminho, 'r')

        for l in dados:
            aux = l.split()
            user = User()
            user.username = aux[0]
            user.email = aux[1]
            user.cpf = aux[2]
            user.password = make_password(aux[2])
            user.save()

        dados.close()
        import os
        from SGEI.settings import BASE_DIR

        os.remove(BASE_DIR / caminho)

        return redirect('accounts:list_user')

    return render(request, 'arquivos/cad.html', context)
"""

def list_users(request):
    context = {}

    users = User.objects.filter(is_staff=True)
    context['list_user'] = users

    return render(request, 'user/list_user.html', context)