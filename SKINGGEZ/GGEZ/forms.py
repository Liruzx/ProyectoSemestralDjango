from dataclasses import fields
from django import forms
from .models import Usuario, Producto

class formRegistro(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

