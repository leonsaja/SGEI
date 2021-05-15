from django.contrib.auth.forms import UserChangeForm
from django import forms
from .models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    Login = forms.CharField(

        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "value": "",
                "class": "form-control"
            }
        ))
    Senha = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Senha",
                "value": "",
                "class": "form-control"
            }
        ))


class CustomUsuarioCreateForm(forms.ModelForm):

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)
    username = forms.CharField(label='Usuário')
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'cpf', 'fone', 'foto')


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Senha não confere |")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUsuarioChangeForm(UserChangeForm):

    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    cpf = forms.CharField(label='CPF')
    fone = forms.CharField(label='Telefone')
    username = forms.CharField(label='Usuário')

    class Meta:
        model = User
        fields =('username', 'email', 'foto', 'first_name', 'last_name', 'cpf', 'fone', 'is_staff')



class UserAdminForm(forms.ModelForm):

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)
    username = forms.CharField(label='Usuário')
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    cpf = forms.CharField(label='CPF')
    fone = forms.CharField(label='Telefone')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'cpf', 'fone', 'is_staff')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Senha não confere |")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user