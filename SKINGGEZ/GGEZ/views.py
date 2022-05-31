from django.shortcuts import render
from .models import Usuario, Producto
from .forms import formRegistro
from django.contrib import messages

# Create your views here.



def paginaPrincipal(request):
    return render(request, 'GGEZ/paginaPrincipal.html')

def Registro(request):

    form = formRegistro(request.POST or None)
    if form.is_valid():
        form.save()		
        messages.success(request, 'Usuario registrado correctamente.')
        form = formRegistro()
    else:
        messages.error(request, 'Error al registrar usuario. Revise los datos.')
    contexto = {'form': form }
        
    return render(request,'GGEZ/Registro.html',contexto)


    
   


    



    




def index(request):
    return render(request,'GGEZ/index.html')

def menuCompraLOL(request):

    productos = Producto.objects.all()
    contexto = {
            'productos' : productos
    }

    return render(request,'GGEZ/menuCompraLOL.html',contexto)

def menuCompraVALO(request):
    return render(request,'GGEZ/menuCompraVALO.html')

def menuCompraCSGO(request):
    return render(request,'GGEZ/menuCompraCSGO.html')

def menuVentaLOL(request):

    if request.POST:
        produ = Producto()
        produ.precio = request.POST.get('precio') 
        produ.nombreSkin = request.POST.get('nombreSkin')       
        produ.nombreUsuario = request.POST.get('nombreUsuario')  
        produ.imagenSkin = request.FILES.get('imagenSkin')

        try:
            produ.save()
            mensaje = 'Publicado correctamente'
        except:
            
            mensaje = 'No se ha publicado correctamente'
 


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


