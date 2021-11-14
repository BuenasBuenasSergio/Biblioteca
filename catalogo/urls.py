from typing import Concatenate
from django.contrib import admin
from django.forms import forms
from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from catalogo.views import todos_libros
from catalogo.views import LibrosListView
from catalogo.views import SearchResultsListView
from catalogo.views import crear_autor 
from catalogo.views import CrearAutor, ListaAutores, eliminarAutor, modificarAutor



urlpatterns = [
    path('libros/', LibrosListView.as_view(), name ='listado_libros'),
    path('buscarlibros/', SearchResultsListView.as_view(), name ='search_results'),
    path('autor/crear', crear_autor, name ='search_results'),
    path('autor/crear2', CrearAutor.as_view(), name='crear_autor2'),
    path('autores/', ListaAutores.as_view(), name='listado_autor'),
    path('eliminarAutor/<int:pk>', eliminarAutor.as_view(), name='eliminar_autor'),
    path('modificarAutor/<int:pk>', modificarAutor.as_view(), name='modificar_autor'),
]