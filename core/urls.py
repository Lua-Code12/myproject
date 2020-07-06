from django.urls import path
from .views import home, formulario, login, compra, catalogo


urlpatterns = [
    path('', home, name="home"),
    path('formulario/', formulario, name="formulario"),
    path('login/', login, name="login"),
    path('compra/', compra, name="compra"),
    path('catalogo/', catalogo, name="catalogo")
]