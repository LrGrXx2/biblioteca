from django.urls import include, path
from catalogo.views import LibrosListView, SearchResultsListView, crear_autor
from catalogo.views import todos_autores

urlpatterns = [
    path('libros/', LibrosListView.as_view(), name='listado_libros'),
    path('autores/', todos_autores, name='listado_autores'),
    path('buscar/', SearchResultsListView.as_view(), name='buscalibros'),
    path('autor/create', crear_autor, name='crear_autor'),
]