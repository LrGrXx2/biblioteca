from django.urls import include, path
from catalogo.views import LibrosListView, SearchResultsListView, crear_autor, crear_libro, CrearAutor, ModificarAutor, EliminarAutor
from catalogo.views import todos_autores

urlpatterns = [
    path('libros/', LibrosListView.as_view(), name='listado_libros'),
    path('autores/', todos_autores, name='listado_autores'),
    path('buscarlibros/', SearchResultsListView.as_view(), name='buscalibros'),
    path('autor/crear', crear_autor, name='crear_autor'),
    path('libro/crear', crear_libro, name='crear_libro'),
    path('autor/crear2', CrearAutor.as_view(), name='crear_autor2'),
    path('autor/modificar/<int:pk>', ModificarAutor.as_view(), name='modificar_autor'),
    path('autor/eliminar/<int:pk>', EliminarAutor.as_view(), name='eliminar_autor'),
]