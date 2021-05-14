from django.urls import path, include
from .views import relatorioedital,pdf_inscricaoDetelhada

app_name = 'relatorios'
urlpatterns = [

    path('pdf/edital/<int:id>', relatorioedital, name='relatorioedital'),
    path('view/inscriçãod/pdf/<int:id>', pdf_inscricaoDetelhada, name='inscricaodetalhada'),

]
