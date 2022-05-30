from django.shortcuts import render
from .models import Usuario

# Create your views here.



def paginaPrincipal(request):
    return render(request, 'GGEZ/paginaPrincipal.html')

def Registro(request):

        nombreUsuario = request.POST['nombre_usuario']
        correo = request.POST['correo']
        fechaNac = request.POST['fecha_na']
        contra = request.POST['contraseña']
        
        
        Usuario.objects.create(nombreUsuario = nombreUsuario, correo = correo, fechaNac = fechaNac, contra = contra )
        
        
        
        return render(request,'GGEZ/Registro.html')


    
   


    



    




def index(request):
    return render(request,'GGEZ/index.html')

def menuCompraLOL(request):
    return render(request,'GGEZ/menuCompraLOL.html')

def menuCompraVALO(request):
    return render(request,'GGEZ/menuCompraVALO.html')

def menuCompraCSGO(request):
    return render(request,'GGEZ/menuCompraCSGO.html')

def menuVentaLOL(request):
    return render(request, 'GGEZ/menuVentaLOL.html')
    
def menuVentaVALO(request):
    return render(request, 'GGEZ/menuVentaVALO.html')

def menuVentaCSGO(request):
    return render(request, 'GGEZ/menuVentaCSGO.html')

def chatCompra(request):
    return render(request, 'GGEZ/chatCompra.html')



def recuperarContrasenia(request):
    return render(request, 'GGEZ/recuperarContrasenia.html')

def cambioDeContrasenia(request):
    return render(request, 'GGEZ/cambioDeContrasenia.html')

def mensajeCambioDeContrasenia(request):
    return render(request, 'GGEZ/mensajeCambioDeContrasenia.html')


