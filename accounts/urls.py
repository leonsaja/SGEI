from django.urls import path, include

from accounts.views import  list_users, login_view, register_user,\
    usuario_edit, edit_password,user_novo, perfil
#create_user_arquivo

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_user, name='register'),
    #path('user/arquivo/', create_user_arquivo, name='create_user_arquivo'),
    path('user/novo/',user_novo,name='add_user'),
    path('user/perfil/', perfil, name='perfil_user'),
    path('user/list/', list_users, name='list_user'),
    path('update/<int:id>', usuario_edit, name='upd_user'),
    path('edit/senha/<int:id>', edit_password, name='edit_senha'),


]
