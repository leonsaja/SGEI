from django.db import models
from accounts.models import User


class Edital(models.Model):

    STATUS_CHOICE = (
        ('ab', 'Aberto'),
        ('em', 'Em Analise'),
        ('fn', 'Finalizado')
    )

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICE, default='ab')
    banner = models.ImageField(upload_to='editais/banner', null=True, blank=True)
    arquivo = models.FileField(upload_to='editais/pdf', null=True, blank=True)

    # ---- Campos para controle de datas de criação e edição ----
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Edital"
        verbose_name = "Editais"

class Pergunta(models.Model):

    edital = models.ForeignKey(Edital, on_delete=models.CASCADE)
    descricao = models.TextField()
    is_aberta = models.BooleanField(default=False, null=True)
    has_arquivo = models.BooleanField(default=False, null=True)

    # ---- Campos para controle de datas de criação e edição ----
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Pergunta"
        verbose_name = "Perguntas"

class Alternativa(models.Model):

    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    descricao = models.TextField()
    peso = models.IntegerField(default=0)
    # ---- Campos para controle de datas de criação e edição ----
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.descricao)

    class Meta:
        verbose_name_plural = "Alternativa"
        verbose_name = "Alternativas"

class Inscricao(models.Model):

    STATUS_CHOICE = (
        ('df', 'Defirido'),
        ('in', 'Indefirido'),
        ('an', 'Em Analise'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    edital = models.ForeignKey(Edital, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICE, default='an')
    nivel_vul = models.IntegerField(default=0)

    # ---- Campos para controle de datas de criação e edição ----
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def nivel(self):
        respostas = list(self.resposta_set.all())

        pontos = 0

        for resp in respostas:

            if resp.alternativa != None  and \
                    resp.alternativa != None:

                pontos += resp.alternativa.peso
        self.nivel_vul = pontos
        self.save()
        return pontos



    def __str__(self):
        return "Aluno " +self.user.first_name + " Numero de inscrição " + str(self.id)

    class Meta:
        verbose_name_plural = "Inscrição"
        verbose_name = "Inscrições"
        ordering = ["-nivel_vul",]


class Resposta(models.Model):

    inscricao = models.ForeignKey(Inscricao, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    alternativa = models.ForeignKey(Alternativa, on_delete=models.CASCADE, null=True, blank=True)
    arquivo = models.FileField(upload_to='inscricoes', null=True, blank=True)
    resposta_aberta = models.TextField(null=True, blank=True)

    # ---- Campos para controle de datas de criação e edição ----
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Resposta"
        verbose_name = "Respostas"


