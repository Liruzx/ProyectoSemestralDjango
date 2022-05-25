from django.urls import path
from .views import paginaPrincipal,Registro

urlpatterns = [
    path('',paginaPrincipal,name="paginaPrincipal"),
    path('Registro/',Registro,name="Registro"),
]