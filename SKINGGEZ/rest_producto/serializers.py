from dataclasses import field
from rest_framework import serializers
from GGEZ.models import Producto,Producto2,Producto3

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['precio', 'nombreSkin', 'nombreUsuario', 'imagenSkin']

class ProductoSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Producto2
        fields = ['precio2', 'nombreSkin2', 'nombreUsuario2', 'imagenSkin2']

class ProductoSerializer3(serializers.ModelSerializer):
    class Meta:
        model = Producto3
        fields = ['precio3', 'nombreSkin3', 'nombreUsuario3', 'imagenSkin3']