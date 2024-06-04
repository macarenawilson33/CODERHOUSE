from django.db import models

# Create your models here.

class Libro (models.Model):   
  nombre = models.CharField (max_length=40)
  AutorLibro= models.CharField (max_length=40) 
  anio_publicacion= models.IntegerField
  
  
class Vinilo (models.Model):
  nombre = models.CharField (max_length=40)
  artista= models.CharField (max_length=40) 
  anio_publicacion= models.IntegerField
   


class Comics (models.Model):
  nombre = models.CharField (max_length=40)
  AutorComic= models.CharField (max_length=40) 
  anio_publicacion= models.IntegerField 
  
    
        