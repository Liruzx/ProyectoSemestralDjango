from django.urls import path
from .views import paginaPrincipal,Registro,index,menuCompraLOL,menuCompraVALO,menuCompraCSGO

urlpatterns = [
    path('',paginaPrincipal,name="paginaPrincipal"),
    path('Registro/',Registro,name="Registro"),
    path('index/',index,name="index"),
    path('menuCompraLOL/',menuCompraLOL,name="menuCompraLOL"),
    path('menuCompraVALO/',menuCompraVALO,name="menuCompraVALO"),
    path('menuCompraCSGO/',menuCompraCSGO,name="menuCompraCSGO"),
    
]