from dataclasses import fields
from django import forms
from .models import Usuario, Producto,Juego,Juego2,Juego3

class formRegistro(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'


class formEditar(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombreUsuario']

class formEditarJuego(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['nombreJuego','imagenJuego']

class formEditarJuego2(forms.ModelForm):
    class Meta:
        model = Juego2
        fields = ['nombreJuego2','imagenJuego2']

class formEditarJuego3(forms.ModelForm):
    class Meta:
        model = Juego3
        fields = ['nombreJuego3','imagenJuego3']


