from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro, Vinilo, Comics
from .forms import LibrosFormulario, VinilosFormulario, ComicsFormulario


# Create your views here.

def libros(req):

  return render(req, "libros.html", {})

def vinilos (req):

  return render(req, "vinilos.html", {})

def comics(req):

  return render(req, "comics.html", {})

def Inicio(req):

  return render(req, "inicio.html", {})


def libros_formulario(req):

  if req.method == 'POST':

    miFormulario = LibrosFormulario(req.POST)

    if miFormulario.is_valid():

      data = miFormulario.cleaned_data
      print(data)

      nuevo_libro = Libro(nombre=data['nombre'], autor=data['autor'])
      nuevo_libro.save()

      return render(req, "inicio.html", {"message": "Libro agregado con éxito"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else: 

    miFormulario = LibrosFormulario()

    return render(req, "libros_formularios.html", {"miFormulario": miFormulario})
 
def vinilo_formulario(req):

  if req.method == 'POST':

    miFormulario = VinilosFormulario(req.POST)

    if miFormulario.is_valid():

      data = miFormulario.cleaned_data

      nuevo_vinilo = Vinilo(nombre=data['nombre'], artista=data['artista'])
      nuevo_vinilo.save()

      return render(req, "inicio.html", {"message": "Vinilo agregado con éxito"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:
    
    miFormulario = VinilosFormulario()

    return render(req, "vinilos_formularios.html", {"miFormulario": miFormulario})
 
def comics_formulario(req):

  if req.method == 'POST':

    miFormulario = ComicsFormulario(req.POST)

    if miFormulario.is_valid():

      data = miFormulario.cleaned_data

      nuevo_comics = Comics(nombre=data['nombre'], autor=data['autor'])
      nuevo_comics.save()

      return render(req, "inicio.html", {"message": "Comic agregado con éxito"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:

    miFormulario = ComicsFormulario()

    return render(req, "comics_formularios.html", {"miFormulario": miFormulario}) 
 



def busqueda_libros(req):

    return render(req, "busqueda_libros.html", {})

def buscarLibro(req):
  if req.GET["Autor"]:
    autor = req.GET["Autor"]
    libro = Libro.objects.filter(AutorLibro__icontains =autor)
    return render(req, "resultadoBusqueda.html", {"libro": libro, "Autor": autor})
  else:
    return render(req, "inicio.html", {"message": "No se ingresaron datos correctos"})

def busqueda_vinilos (req):

    return render(req, "busqueda_vinilos.html", {})

def buscarVinilo(req):


  if req.GET["Artista"]:

    artista = req.GET["Artista"]

    vinilo = Vinilo.objects.filter(artista__icontains = artista)

    return render(req, "resultadoBusquedavinilos.html", {"vinilo": vinilo, "Artista": artista })

  else:
      
      return render(req, "inicio.html", {"message": "No se ingresaron datos correctos"})


def busqueda_comics(req):

    return render(req, "busqueda_comics.html", {})

def buscarComic(req):


  if req.GET["Autor"]:

    autor = req.GET["Autor"]

    comics = Comics.objects.filter(AutorComic__icontains =autor)

    return render(req, "resultadoBusquedacomics.html", {"comics": comics, "Autor": autor})

  else:
      
      return render(req, "inicio.html", {"message": "No se ingresaron datos correctos"})
