from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UsuarioManager(BaseUserManager):

    def create_user(self, email, username, first_name, last_name, cpf, password=None):
        if not email:
            raise ValueError('Os usuários devem ter um endereço de email')
        if not username:
            raise ValueError('Os usuários devem ter um nome de usuário')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            cpf=cpf,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, first_name, last_name, cpf):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            cpf=cpf,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):

    username = models.CharField('Usuario', max_length=25, unique=True)
    email = models.EmailField('E-mail', unique=True)
    foto = models.ImageField(blank=True, upload_to='user_foto', verbose_name='Foto', null='True')
    fone = models.CharField('Telefone', max_length=15)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    is_staff = models.BooleanField('Membro da equipe', default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'cpf']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural ="Usuario"
        verbose_name ='Usuarios'

    objects = UsuarioManager()


