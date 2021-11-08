from django.urls import include, path
from catalogo.views import LibrosListView
from catalogo.views import todos_autores

urlpatterns = [
    path('libros/', LibrosListView.as_view(), name='listado_libros'),
    path('autores/', todos_autores, name='listado_autores'),
]