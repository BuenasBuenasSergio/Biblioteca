from django.db import models
from django.shortcuts import redirect, render
#from django.http import HttpResponse
from catalogo.models import Book
from catalogo.models import Author
from django.views import generic
from django.views.generic import ListView
from catalogo.forms import AuthoForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

def indice(request):
        '''Pagina Inicial de nuestra Web'''
        #libros = Book.objects.all()
        #sautores = Author.objects.all()
        
        datos = {'autores' : autores}

        busqueda = request.GET.get('q')

        if busqueda:
                libros = Book.objects.filter(title__icontains = busqueda)
                datos['noencontrado'] = True
        else:
            libros = Book.objects.all()

        datos['libros'] = libros
        datos = {'author': 'Alejandro Dumas', 'libros' : libros}

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


#Crear Autor Manual
def crear_autor(request):

    if request.method == 'POST':
        form = AuthoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Autor Creado')
            return redirect('/')
        else:
            form = AuthoForm()
    datos={'form': AuthoForm}
    return render(request, 'crear_autor.html', context=datos)

#Lista de libros Generica
class LibrosListView(generic.ListView):
    '''Creacion de Vista Generica'''
    model = Book
    paginate_by = 15

#Buscar libro vista generica
class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'catalogo/search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Book.objects.filter(title__icontains=query)

#Crear autor vista generica
class CrearAutor(SuccessMessageMixin, generic.CreateView):
    model = Author
    fields = '__all__'
    template_name = 'crear_autor.html'
    success_url = 'catalogo/autores/'
    success_message = "%(first_name)s %(last_name)s se ha creado correctamente"

#Listar Author vista generica
class ListaAutores(ListView):
    '''Vista Generica Autores'''
    model = Author
    paginate_by = 15

#Eliminar Autores
class eliminarAutor(SuccessMessageMixin, generic.DeleteView):
    model = Author
    success_url = '/'
    success_message = "%(first_name)s %(last_name)s se ha borrado correctamente"
    template_name = 'autor_confirmar_borrado.html'


#Modificar Autor de manera Automatica
class modificarAutor(SuccessMessageMixin, generic.UpdateView):
    model = Author
    fields = '__all__'
    success_url = 'catalogo/autores'
    template_name = 'modificar_autor.html'
    success_message = "%(first_name)s %(last_name)s se ha modificado correctamente"