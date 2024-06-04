from django.contrib import admin
from django.urls import path
from AppEntrega.views import (
    Inicio,
    libros, 
    vinilos, 
    comics, 
    libros_formulario, 
    vinilo_formulario, 
    comics_formulario, 
    busqueda_libros, 
    buscarLibro,
    buscarVinilo,
    busqueda_vinilos,
    buscarComic,    
    busqueda_comics
    )

urlpatterns = [
    path('inicio/', Inicio, name='Inicio'),
    path('libros/', libros, name='Libro'),
    path('vinilos/', vinilos, name='Vinilo'),
    path('comics/', comics, name='Comics'),
    path('libros-formulario/', libros_formulario, name='LibrosFormulario'),
    path('vinilos-formulario/', vinilo_formulario, name='VinilosFormulario'),
    path('comics-formulario/', comics_formulario, name='ComicsFormulario'),
    path('busqueda-libros/', busqueda_libros, name='BusquedaLibros'),
    path('buscar-libro/', buscarLibro, name='BuscarLibros'),
    path('busqueda-vinilos/', busqueda_vinilos, name='BusquedaVinilos'),
    path('buscar-vinilo/', buscarVinilo, name='BuscarVinilos'),
    path('busqueda-comics/', busqueda_comics, name='BusquedaComics'),
    path('buscar-comic', buscarComic, name='BuscarComics'),
]
