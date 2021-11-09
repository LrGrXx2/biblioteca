from django.forms import ModelForm
from catalogo.models import Author
#https://developer.mozilla.org/es/docs/Learn/Server-side/Django/forms

class AuthorForm(ModelForm):
    '''Formulario para crear autores'''
    class Meta:
        model = Author
        fields = '__all__'