from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'loja/inicio.html')

def produtos(request):
    return render(request, 'loja/produtos.html')