from django.urls import path
from .views import home,mylogout,index

app_name = 'core'

urlpatterns = [
    path('',home, name='home'),
    path('index/', index, name='index'),
    path('logout/', mylogout, name="mylogout"),
]
