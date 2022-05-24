from django.urls import path
from .views import paginaPrincipal

urlpatterns = [
    path('',paginaPrincipal,name="paginaPrincipal"),
]