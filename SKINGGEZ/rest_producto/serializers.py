from dataclasses import field
from rest_framework import serializers
from GGEZ.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['precio', 'nombreSkin', 'nombreUsuario', 'imagenSkin']