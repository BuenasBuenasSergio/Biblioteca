from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from catalogo.views import todos_libros
from catalogo.views import LibrosListView
from catalogo.views import SearchListView
import debug_toolbar


urlpatterns = [
    path('libros/', LibrosListView.as_view(), name ='listado_libros'),
    path('busqueda/', SearchListView.as_view(), name ='search_results'),
]