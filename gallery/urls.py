from django.urls import path
from gallery.views import index, imagem, buscar

#lista de Urls 
urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name="buscar"),
]