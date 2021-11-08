from django.shortcuts import render
from catalogo.models import Author, Book
from django.views import generic

# from django.http import HttpResponse

# Create your views here.

#Vistas tipo función

def indice(request):
    libros = Book.objects.all()
    datos = {'autor': 'Luis Miguel', 'libros': libros}
    return render(request, 'index.html', context=datos)

def todos_libros(request):
    libros=Book.objects.all().order_by('title')
    return render(request, 'todos_libros.html', context={'libros':libros})

def todos_autores(request):
    autores=Author.objects.all().order_by('first_name')
    return render(request, 'todos_autores.html', context={'autores':autores})

class LibrosListView(generic.ListView):
    '''Vista genérica para nuestro listado de libros'''
    model = Book
    paginate_by = 15