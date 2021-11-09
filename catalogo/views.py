from django.db import models
from django.shortcuts import render
#from django.http import HttpResponse
from catalogo.models import Book
from catalogo.models import Author
from django.views import generic


# Create your views here.

def indice(request):
        '''Pagina Inicial de nuestra Web'''
        # libros = Book.objects.all()
        # autores = Author.objects.all()
        
        datos = {'autores' : autores}

        busqueda = request.GET.get('q')

        if busqueda:
                libros = Book.objects.filter(title__icontains = busqueda)
                datos['noencontrado'] = True
        else:
                libros = Book.objects.all()

        datos['libros'] = libros
       # datos = {'author': 'Alejandro Dumas', 'libros' : libros}

        return render(request, 'index.html', context=datos)


def autores(request):
    autores = Author.objects.all()

    datos = {
        'autores': autores
        # la primera parte del diccionario es para llamar en el view
    }
    return render(request, 'autores.html', context=datos)


def contact(request):
    return render(request, 'contacto.html')


def todos_libros(request):

    libros = Book.objects.all().order_by('title')
    return render(request, 'todos_libros.html', context={'libros': libros})


class LibrosListView(generic.ListView):
    '''Creacion de Vista Generica'''
    model = Book
    paginate_by = 15

class SearchListView(generic.ListView):

    model = Book
    context_object_name = 'book_list'
    template_name = 'libros/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(title_icotains = query)


