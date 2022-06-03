from django.shortcuts import redirect, render,get_object_or_404
from .models import Usuario, Producto,Producto2,Producto3
from .forms import formRegistro
from django.contrib import messages

# Create your views here.



def paginaPrincipal(request):
    
    

    if request.method == 'POST':
       
        try:
            detalleUsuario=Usuario.objects.get(nombreUsuario=request.POST.get('nombreUsuario'),contra =request.POST.get('contra'))

            request.session['nombreUsuario']= detalleUsuario.nombreUsuario
            user = Usuario.objects.all()
            contexto = {
                'user':user
            }
            if request.POST.get('nombreUsuario') == "ELPEPE" and request.POST.get('contra') == "ELPEPE123":

                return render(request,'GGEZ/vistaAdmin/index_Admin.html',contexto)
            else:

                return render(request,'GGEZ/index.html',contexto)
           
        except Usuario.DoesNotExist as o:
            messages.success(request, 'Nombre de usuario o Contraseña son incorrectos')
    #elif request.method == 'POST':
     #   try:
      #      detalleUsuario=Usuario.objects.get(nombreUsuario=admin,contra = contraAdmin)
       #     request.session['nombreUsuario']= detalleUsuario.nombreUsuario
        #    user = Usuario.objects.all()
         #   contexto = {
          #      'user':user
           # }

            #return render(request,'GGEZ/vistaAdmin/menuCompraLOL_Admin.html',contexto)
        #except Usuario.DoesNotExist as o:
         #   messages.success(request, 'Nombre de usuario o Contraseña son incorrectos')
    
    
            

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
    
    user = Usuario.objects.all()
    contexto = {
                'user':user
            }
    

    
    return render(request,'GGEZ/index.html',contexto)

def menuCompraLOL(request):

    productos = Producto.objects.all()
    contexto = {
            'productos' : productos
    }

    return render(request,'GGEZ/menuCompraLOL.html',contexto)

def menuCompraVALO(request):

    productos2 = Producto2.objects.all()
    contexto = {
            'productos2' : productos2
    }

    return render(request,'GGEZ/menuCompraVALO.html',contexto)

def menuCompraCSGO(request):

    productos3 = Producto3.objects.all()
    contexto = {
            'productos3' : productos3
    }

    return render(request,'GGEZ/menuCompraCSGO.html',contexto)

def menuVentaLOL(request):

    if request.POST:
        produ = Producto()
        produ.precio = request.POST.get('precio') 
        produ.nombreSkin = request.POST.get('nombreSkin')       
        produ.nombreUsuario = request.POST.get('nombreUsuario')  
        produ.imagenSkin = request.FILES.get('imagenSkin')

        try:
            produ.save()
            messages.success(request, 'Se ha publicado Correctamente')
        except:
            
             messages.success =(request, 'No se ha publicado correctamente')
 


    return render(request, 'GGEZ/menuVentaLOL.html')
    



def menuVentaVALO(request):

    if request.POST:
        produ = Producto2()
        produ.precio2 = request.POST.get('precio') 
        produ.nombreSkin2 = request.POST.get('nombreSkin')       
        produ.nombreUsuario2 = request.POST.get('nombreUsuario')  
        produ.imagenSkin2 = request.FILES.get('imagenSkin')

        try:
            produ.save()
            messages.success(request, 'Se ha publicado Correctamente')
        except:
            
             messages.success =(request, 'No se ha publicado correctamente')



    return render(request, 'GGEZ/menuVentaVALO.html')

def menuVentaCSGO(request):

    if request.POST:
        produ = Producto3()
        produ.precio3 = request.POST.get('precio') 
        produ.nombreSkin3 = request.POST.get('nombreSkin')       
        produ.nombreUsuario3 = request.POST.get('nombreUsuario')  
        produ.imagenSkin3 = request.FILES.get('imagenSkin')

        try:
            produ.save()
            messages.success(request, 'Se ha publicado Correctamente')
        except:
            
             messages.success =(request, 'No se ha publicado correctamente')






    return render(request, 'GGEZ/menuVentaCSGO.html')

def chatCompra(request):
    return render(request, 'GGEZ/chatCompra.html')



def recuperarContrasenia(request):
    return render(request, 'GGEZ/recuperarContrasenia.html')

def cambioDeContrasenia(request):
    return render(request, 'GGEZ/cambioDeContrasenia.html')

def mensajeCambioDeContrasenia(request):
    return render(request, 'GGEZ/mensajeCambioDeContrasenia.html')

def eliminarProducto (request, id):
    produ = Producto.objects.get(id=id)
    try:
        produ.delete()
        
    except:
        
        messages.error(request,'')
        
    return render(request,'GGEZ/vistaAdmin/menuCompraLOL_Admin.html')

def eliminarProducto2 (request, id):
    produ = Producto2.objects.get(id=id)
    try:
        produ.delete()
       
    except:
        
        messages.error(request,'')
        
    return render(request,'GGEZ/vistaAdmin/menuCompraVALO_Admin.html')

def eliminarProducto3 (request, id):
    produ = Producto3.objects.get(id=id)
    try:
        produ.delete()
        messages.success(request,'')
    except:
        
        messages.error(request,'')
        
    return render(request,'GGEZ/vistaAdmin/menuCompraCSGO_Admin.html')


def editarUsuario (request, id):

    user = Usuario.objects.get(id=id)
    form = formRegistro(request.POST, instance=user)
    if form.is_valid():
        form.save()
    user = Usuario.objects.all()
    
    

    
    return render(request,'GGEZ/editarUsuario.html')

    #usuario = Usuario.objects.filter(id=id).first()

    #form = formRegistro(instance=usuario)
    

    #return render(request,'GGEZ/editarUsuario.html',{"form" : form, 'usuario':usuario})

#def actualizarUsuario (request, id):
 #   user = Usuario.objects.get(id=id)
  #  form = formRegistro(request.POST, instance=user)
   # if form.is_valid():
    #    form.save()
    #user = Usuario.objects.all()
    
    

    
    #return redirect(to='index')



#VISTAS DEL ADMIN




def menuCompraLOL_Admin(request):

    productos = Producto.objects.all()
    contexto = {
            'productos' : productos
    }

    return render(request,'GGEZ/vistaAdmin/menuCompraLOL_Admin.html',contexto)


def menuCompraVALO_Admin(request):

    productos2 = Producto2.objects.all()
    contexto = {
            'productos2' : productos2
    }

    return render(request,'GGEZ/vistaAdmin/menuCompraVALO_Admin.html',contexto)

def menuCompraCSGO_Admin(request):

    productos3 = Producto3.objects.all()
    contexto = {
            'productos3' : productos3
    }

    return render(request,'GGEZ/vistaAdmin/menuCompraCSGO_Admin.html',contexto)

def index_Admin(request):

    user = Usuario.objects.all()
    contexto = {
                'user':user
            }

    return render(request,'GGEZ/vistaAdmin/index_Admin.html',contexto)


def menuVentaLOL_Admin(request):

    if request.POST:
        produ = Producto()
        produ.precio = request.POST.get('precio') 
        produ.nombreSkin = request.POST.get('nombreSkin')       
        produ.nombreUsuario = request.POST.get('nombreUsuario')  
        produ.imagenSkin = request.FILES.get('imagenSkin')

        try:
            produ.save()
            messages.success(request, 'Se ha publicado Correctamente')
        except:
            
             messages.success =(request, 'No se ha publicado correctamente')
 


    return render(request, 'GGEZ/vistaAdmin/menuVentaLOL_Admin.html')


def menuVentaVALO_Admin(request):

    if request.POST:
        produ = Producto2()
        produ.precio2 = request.POST.get('precio') 
        produ.nombreSkin2 = request.POST.get('nombreSkin')       
        produ.nombreUsuario2 = request.POST.get('nombreUsuario')  
        produ.imagenSkin2 = request.FILES.get('imagenSkin')

        try:
            produ.save()
            messages.success(request, 'Se ha publicado Correctamente')
        except:
            
             messages.success =(request, 'No se ha publicado correctamente')



    return render(request, 'GGEZ/vistaAdmin/menuVentaVALO_Admin.html')


def menuVentaCSGO_Admin(request):

    if request.POST:
        produ = Producto3()
        produ.precio3 = request.POST.get('precio') 
        produ.nombreSkin3 = request.POST.get('nombreSkin')       
        produ.nombreUsuario3 = request.POST.get('nombreUsuario')  
        produ.imagenSkin3 = request.FILES.get('imagenSkin')

        try:
            produ.save()
            messages.success(request, 'Se ha publicado Correctamente')
        except:
            
             messages.success =(request, 'No se ha publicado correctamente')






    return render(request, 'GGEZ/vistaAdmin/menuVentaCSGO_Admin.html')



def chatCompra_Admin(request):
    return render(request, 'GGEZ/vistaAdmin/chatCompra.html')