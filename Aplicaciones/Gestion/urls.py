from django.urls import path
from .views import categoriaEndpoint, productoEndpoint

urlpatterns = [
    path('categorias/', categoriaEndpoint),
    path('productos/', productoEndpoint),
]
