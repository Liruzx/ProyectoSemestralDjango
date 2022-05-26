from django.shortcuts import render

# Create your views here.



def paginaPrincipal(request):
    return render(request, 'GGEZ/paginaPrincipal.html')

def Registro(request):
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
