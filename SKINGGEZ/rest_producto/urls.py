from django.urls import URLPattern, path
from rest_producto.views import lista_productos,detalle_producto, lista_productos2,detalle_producto2,lista_productos3,detalle_producto3


urlpatterns = [
    
    path('lista_productos', lista_productos,name="lista_productos"),
    path('detalle_producto/<id>',detalle_producto, name="detalle_producto"),


    #producto 2
    
    path('lista_productos2', lista_productos2,name="lista_productos2"),
    path('detalle_producto2/<id>',detalle_producto2, name="detalle_producto2"),

    #producto 3

    path('lista_productos3', lista_productos3,name="lista_productos3"),
    path('detalle_producto3/<id>',detalle_producto3, name="detalle_producto3"),



]