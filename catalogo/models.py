'''
0. Recuerda añadir app a installed apps (settings dentro de biblioteca)
1. Definir modelos
2. py manage.py migrate
'''

from django.db import models
from django.db.models.base import Model

# Create your models here.
class Genre(models.Model):
    name = models.CharField("Nombre género", max_length = 200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Género'

#------------------------------------------------------------

class Author(models.Model):
    first_name = models.CharField("Nombre", max_length = 100)
    last_name = models.CharField("Apellido", max_length = 100)
    date_of_birth = models.DateField('Fecha de nacimiento', null = True, blank = True)
    date_of_death = models.DateField('Fallecido', null = True, blank = True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

#------------------------------------------------------------

class Book(models.Model):
    '''
    Libro para aplicación de biblioteca ...
    '''
    title = models.CharField('Título', max_length = 250)
    sumary = models.TextField('Resumen', blank = True)
    isbn = models.CharField(max_length = 13, blank = True)
    fecha = models.DateField(blank = True, null = True, help_text = 'Fecha de publicación')


    # faltan las relaciones
    author = models.ForeignKey('Author', on_delete = models.SET_NULL, null = True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def muestra_genero(self):
        '''Muestra género para admin'''
        return ', '.join([gen.name for gen in self.genre.all()[:1]])

    muestra_genero.short_description = 'Género'

    class Meta:
        verbose_name = 'Libro'

# IDIOMAS
class Languaje(models.Model):
    name = models.CharField("Idioma", max_length = 80)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Idioma'

# FORMULARIO DE CONTACTO

from django import forms

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)