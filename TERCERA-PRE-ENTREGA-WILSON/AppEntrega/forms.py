from django import forms
 
class LibrosFormulario (forms.Form):
    nombre = forms.CharField(max_length=200)
    autor = forms.CharField(max_length=200)
 
class VinilosFormulario (forms.Form):
    nombre = forms.CharField(max_length=200)
    artista = forms.CharField(max_length=40)

class ComicsFormulario (forms.Form):
    nombre = forms.CharField(max_length=200)
    autor = forms.CharField(max_length=200)