from django.shortcuts import render
from catalogo.models import Author, Book
from django.views import generic
from catalogo.forms import AuthorForm

# from django.http import HttpResponse

# Create your views here.

#Vistas tipo función

def indice(request):
    datos = {'autor': 'Luis Miguel'}
    busqueda = request.GET.get('q')
    if busqueda:
        libros = Book.objects.filter(title__icontains = busqueda)
        datos['noencontrado'] = True
    else:
        libros = Book.objects.all()

    datos['libros'] = libros

    libros = Book.objects.all()
    
    return render(request, 'index.html', context = datos)


def todos_libros(request):
    libros = Book.objects.all().order_by('title')
    return render(request, 'todos_libros.html', context = {'libros':libros})


def todos_autores(request):
    autores = Author.objects.all().order_by('first_name')
    return render(request, 'todos_autores.html', context = {'autores':autores})

#creación autor
def crear_autor(request):
    datos = {'form': AuthorForm()}
    return render(request, 'crear_autor.html', context = datos)


class LibrosListView(generic.ListView):
    '''Vista genérica para nuestro listado de libros'''
    model = Book
    paginate_by = 15


class SearchResultsListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Book.objects.filter(title__icontains = query)