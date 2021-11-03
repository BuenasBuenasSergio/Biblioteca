from django.shortcuts import render
#from django.http import HttpResponse
from catalogo.models import Book

# Create your views here.

def indice(request):
    '''Pagina Inicial de nuestra Web'''

    libros = Book.objects.all()
    datos = {'author':'Alejandro Dumas',
            'libros' : libros}
    
    return render(request, 'index.html', context=datos)