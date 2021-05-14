
# Register your models here.
from django.contrib import admin
from .models   import Edital, Pergunta, Alternativa, Inscricao, Resposta

@admin.register(Edital)
class EditalAdmin(admin.ModelAdmin):
    model =Edital
    list_display = ('titulo', 'descricao','status')


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    model =Pergunta
    list_display = ('edital', 'descricao')

@admin.register(Alternativa)
class AlternativaAdmin(admin.ModelAdmin):
    model =Alternativa
    list_display = ('pergunta','descricao')

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    model =Inscricao
    list_display = ('user','edital','status')

@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    model =Resposta
    list_display = ('inscricao','pergunta')


