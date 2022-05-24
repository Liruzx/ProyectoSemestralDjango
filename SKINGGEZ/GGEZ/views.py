from django.shortcuts import render

# Create your views here.



def paginaPrincipal(request):
    return render(request, 'GGEZ/paginaPrincipal.html')