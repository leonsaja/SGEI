from django import forms
"""from material.base import Layout, Fieldset, Row """

from .models import Pergunta, Edital, Alternativa, Resposta, Inscricao

class PerguntaForm(forms.ModelForm):
    is_aberta = forms.BooleanField(required=False, label='Esta pergunta é aberta')
    has_arquivo = forms.BooleanField(required=False, label='Esta pergunta requer arquivos')

    class Meta:
        model = Pergunta
        fields = ('descricao', 'is_aberta', 'has_arquivo')

class AlternativaForm(forms.ModelForm):
    class Meta:
        model = Alternativa
        fields = '__all__'

class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = '__all__'


class EditalForm(forms.ModelForm):
    class Meta:
        model = Edital
        fields = '__all__'



class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = '__all__'



class IncricaoFormAv(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ('status',)