from django.urls import path
from .views import * 
#paginaPrincipal,Registro,index,menuCompraLOL,menuCompraVALO,menuCompraCSGO,menuVentaLOL

urlpatterns = [
    path('',paginaPrincipal,name="paginaPrincipal"),
    path('Registro/',Registro,name="Registro"),
    path('index/',index,name="index"),
    path('menuCompraLOL/',menuCompraLOL,name="menuCompraLOL"),
    path('menuCompraVALO/',menuCompraVALO,name="menuCompraVALO"),
    path('menuCompraCSGO/',menuCompraCSGO,name="menuCompraCSGO"),
    path('menuVentaLOL/',menuVentaLOL,name="menuVentaLOL"),
    path('menuVentaVALO/',menuVentaVALO,name="menuVentaVALO"),
    path('menuVentaCSGO/',menuVentaCSGO,name="menuVentaCSGO"),
    path('chatCompra/',chatCompra,name="chatCompra"),
    path('recuperContrasenia/',recuperarContrasenia,name="recuperarContrasenia"),
    path('cambioDeContrasenia/',cambioDeContrasenia,name="cambioDeContrasenia"),
    path('mensajeCambioDeContrasenia/',mensajeCambioDeContrasenia,name="mensajeCambioDeContrasenia"),

    path('eliminarProducto/<id>/',eliminarProducto,name="eliminarProducto"),
    
    path('eliminarProducto2/<id>/',eliminarProducto2,name="eliminarProducto2"),
    
    path('eliminarProducto3/<id>/',eliminarProducto3,name="eliminarProducto3"),

    
    path('editarUsuario/<id>/',editarUsuario,name="editarUsuario"),
    #path('actualizarUsuario/<id>/',actualizarUsuario,name="actualizarUsuario"),
    

    #URL VISTAS DE ADMIN

    path('menuCompraLOL_Admin/',menuCompraLOL_Admin,name="menuCompraLOL_Admin"),
    path('menuCompraVALO_Admin/',menuCompraVALO_Admin,name="menuCompraVALO_Admin"),
    path('menuCompraCSGO_Admin/',menuCompraCSGO_Admin,name="menuCompraCSGO_Admin"),

    path('index_Admin/',index_Admin,name="index_Admin"),
    
    #URL VENTAS ADMIN

    path('menuVentaLOL_Admin',menuVentaLOL_Admin,name="menuVentaLOL_Admin"),
    path('menuVentaVALO_Admin',menuVentaVALO_Admin,name="menuVentaVALO_Admin"),
    path('menuVentaCSGO_Admin',menuVentaCSGO_Admin,name="menuVentaCSGO_Admin"),

    path('chatCompra_Admin',chatCompra_Admin,name="chatCompra_Admin"),

    path('bloquearUsuario',bloquear,name="bloquear"),

    path('editarJuego/<id>/',editarJuego,name="editarJuego"),
    path('editarJuego2/<id>/',editarJuego2,name="editarJuego2"),
    path('editarJuego3/<id>/',editarJuego3,name="editarJuego3"),

    
]