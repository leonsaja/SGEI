from django.urls import path, include

from .views import EditalList, edital_view_adm, edital_add, edital_delete, edital_edit, \
    inscricao_view, edital_view, \
    pergunta_add, pergunta_edit, pergunta_delete, inscricao_do, inscricao_list_user, edital_list_adm, \
    inscricao_view_user, edital_list_aluno, resultado_edital, inscricao_edit, inscricao_list

app_name='editais'
urlpatterns = [

    #----------------Edital-------------------
    path('', edital_list_adm, name='edital_list'),
    path('view/edital/<int:id>', edital_view_adm, name='edital_view'),
    path('add/edital/', edital_add, name="edital_add"),
    path('edit/edital/<int:id>', edital_edit, name="edital_edit"),
    path('delete/edital/<int:id>', edital_delete, name='edital_delete'),

    path('alunos/edital/list/', edital_list_aluno, name='edital_list_inscri'),
    path('alunos/edital/<int:id>', edital_view, name='edital_view_inscri'),

    path('resultado/edital/<int:id>', resultado_edital, name='resultado_edital'),

    #----------------Pergunta-------------------
    path('add/pergunta/<int:id_edital>', pergunta_add, name="pergunta_add"),
    path('edit/pergunta/<int:id>', pergunta_edit, name="pergunta_edit"),
    path('delete/pergunta/<int:id>', pergunta_delete, name='pergunta_delete'),


    #----------------Incrições-------------------
    path('inscricao/', inscricao_list, name='inscricao_list'),
    path('view/inscricao/<int:id>', inscricao_view, name='inscricao_view'),
    path('alunos/inscricao/<int:id>', inscricao_view_user, name='inscricao_view_user'),
    path('alunos/inscricao/', inscricao_list_user, name='inscricao_list_user'),


    path('inscricao/do/<int:id_edital>', inscricao_do, name='inscricao_do'),
    path('inscricao/edit/<int:id>', inscricao_edit, name='inscricao_edit'),
]