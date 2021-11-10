from django.shortcuts import render, redirect
from catalogo.models import Author, Book
from django.views import generic
from catalogo.forms import AuthorForm, BookForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# from django.http import HttpResponse

# Create your views here.

#Vistas tipo función

def indice(request):
    '''
    Página inicial de nuestra web
    '''
    datos = {'autor': 'Luis Miguel'}
    
    # últimos 5 libros del catálogo
    libros = Book.objects.all().order_by('-id')[:5]

    datos['libros'] = libros

    return render(request, 'index.html',
        context=datos)


def todos_libros(request):
    libros = Book.objects.all().order_by('title')
    return render(request, 'todos_libros.html', context = {'libros':libros})


def todos_autores(request):
    autores = Author.objects.all().order_by('first_name')
    return render(request, 'todos_autores.html', context = {'autores':autores})

#creación autor
def crear_autor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Autor creado correctamente')
            return redirect('/')
    else:
        form = AuthorForm()
    datos = {'form': AuthorForm()}
    return render(request, 'crear_autor.html', 
        context=datos)


#creación libro
def crear_libro(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'El libro ha sido creado correctamente')
            return redirect('/')
    else:
        form = BookForm()
    datos = {'form': BookForm()}
    return render(request, 'crear_libro.html', 
        context=datos)


# Creación de autor con CreateVio. Añadimos SuccessMesaageMixin para mensaje de éxito.
class CrearAutor(SuccessMessageMixin, generic.CreateView):
    model = Author
    fields = '__all__'
    template_name = 'crear_autor.html'
    success_url = '/'
    success_message = "%(first_name)s %(last_name)s se ha creado correctamente"


class CrearLibro(SuccessMessageMixin, generic.CreateView):
    model = Book
    fields = '__all__'
    template_name = 'crear_libro.html'
    success_url = '/'
    success_message = "%(title)s se ha creado correctamente"
    

# Creación de autor con CreateVio. Añadimos SuccessMesaageMixin para mensaje de éxito.
class ModificarAutor(SuccessMessageMixin, generic.UpdateView):
    model = Author
    fields = '__all__'
    template_name = 'modificar_autor.html'
    success_url = '/'
    success_message = "%(first_name)s %(last_name)s se ha modificado correctamente"


# Creación de autor con CreateVio. Añadimos SuccessMesaageMixin para mensaje de éxito.
class EliminarAutor(SuccessMessageMixin, generic.DeleteView):
    model = Author
    success_url = '/'
    success_message = "%(first_name)s %(last_name)s se ha borrado correctamente"
    template_name = 'autor_confirmar_borrado.html'


class LibrosListView(generic.ListView):
    '''Vista genérica para nuestro listado de libros'''
    model = Book
    paginate_by = 15


class AutoresListView(generic.ListView):
    '''
    Vista genérica para nuestro listado de autores
    '''
    model = Author
    paginate_by = 15
    queryset = Author.objects.all().order_by('last_name', 'first_name')


class SearchResultsListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Book.objects.filter(title__icontains = query)