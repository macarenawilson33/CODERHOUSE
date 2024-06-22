from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from django.forms import ModelForm
from .models import Product, Comment

class ChangePasswordForm(SetPasswordForm):
	class Meta:
		model=User
		fields = ['new_password1', 'new_password2']

	def __init__(self, *args, **kwargs):
		super(ChangePasswordForm, self).__init__(*args, **kwargs)

		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Nuevo Password'
		self.fields['new_password1'].label = ''
		self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Su nuevo password no puede ser similar a su otra información.</li><li>Debe contener al menos 8 caracteres.</li><li>No puede ser completamente numérico.</li></ul>'

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Repita el Nuevo Password'
		self.fields['new_password2'].label = ''
		self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Ingrese el mismo password para verificacion.</small></span>'


class UpdateUserForm(UserChangeForm):
	password = None
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def __init__(self, *args, **kwargs):
		super(UpdateUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requerido. 150 caracteres máximo. Letras, dígitos y @/./+/-/_ solamente.</small></span>'


class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requerido. 150 caracteres máximo. Letras, dígitos y @/./+/-/_ solamente.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Su password no puede ser similar a su otra información.</li><li>Debe contener al menos 8 caracteres.</li><li>No puede ser completamente numérico.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Repita el Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Ingrese el mismo password para verificacion.</small></span>'

class ProductForm(ModelForm):
	name = forms.CharField(label="",max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
	description = forms.CharField(label="", max_length=500, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripcion'}))
	price = forms.DecimalField(label="",  decimal_places=2, max_digits=12, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Precio'}))
	image = forms.ImageField()
	#date_created = forms.DateTimeField()
	
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		self.fields['image'].required = False

	class Meta:
		model = Product
		fields = ['name','description','price','image','product_category']

class UpdateProductForm(ModelForm):
	name = forms.CharField(label="",max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
	description = forms.CharField(label="", max_length=500, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripcion'}))
	price = forms.DecimalField(label="",  decimal_places=2, max_digits=12, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Precio'}))
	image = forms.ImageField()

	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		self.fields['image'].required = False

	class Meta:
		model = Product
		fields = ['name','description','price','image','product_category']	
		
			
class CommentForm(ModelForm):
	comment_content = forms.CharField(label="",max_length=500, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese un comentario aqui'}))
	
	class Meta:
		model = Comment
		fields = ['comment_content']