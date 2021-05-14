from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from .models import User


@admin.register(User)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = User
    list_display = ('email','first_name','cpf', 'fone', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'cpf','fone','foto')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
