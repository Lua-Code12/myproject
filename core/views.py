from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    return render(request, 'core/home.html')


def formulario(request):
    return render(request, 'core/formulario.html')

def login(request):
    return render(request, 'core/login.html')

def compra(request):
    return render(request, 'core/compra.html')

def catalogo(request):
    url_get_proveedor = "http://54.90.39.252/api/Producto"
    results = requests.get(url_get_proveedor).json()
    productos = []
    for result in results:
        producto = []
        producto.append(result["descripcion"])
        producto.append(result["precio"])
        producto.append(result["stock"])
        producto.append(result["codigo"])
        productos.append(producto)
    print (productos)
    return render(request, 'core/catalogo.html', {'productos': productos})


   