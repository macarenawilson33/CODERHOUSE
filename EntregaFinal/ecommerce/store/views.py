from django.shortcuts import render, redirect
from .models import Product, ProductCategory, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ProductForm, UpdateUserForm, ChangePasswordForm, UpdateProductForm, CommentForm
from django import forms

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Sesion Iniciada Correctamente')
            return redirect('home')
        else:
            messages.success(request, 'Credenciales Incorrectas, intente otra vez.')
            return redirect('login')
    else:        
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'Sesion Cerrada Correctamente')
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Registro Correcto!')
                return redirect('home')
        else:
            messages.success(request, 'Hubo un problema en el registro, por favor intente otra vez.')

    return render(request, 'register.html', {'form':form})



def category(request, var):
    var = var.replace('-',' ')
    category_display_name = ''
    try:
        if var == 'TODOS':
            products = Product.objects.all()
            category_display_name = 'Todos Los Productos'
        else:
            category = ProductCategory.objects.get(name=var)
            category_display_name = str(category.name).capitalize() + 's'
            products = Product.objects.filter(product_category=category)

        return render(request, 'category.html', {'products':products, 'category_name':category_display_name})
    except :
        messages.error(request, f'Categoria {var} Inexistente')
        return redirect('home')
    
def new_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto dado de alta correctamente')
            return redirect('new_product')
        else:
            messages.error(request, 'Hubo un problema al dar de alta el producto')

    return render(request, 'new_product.html', {'form':form})

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        updateUserForm = UpdateUserForm(request.POST or None, instance=current_user)
        if updateUserForm.is_valid():
            updateUserForm.save()

            login(request, current_user)
            messages.success(request, "Usuario actualizado correctamente")
            return redirect('home')
        return render(request, 'update_user.html', {'form':updateUserForm}) 
    else:
        messages.success(request, "No Autorizado")
        return redirect('home')

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"El password fue cambiado con exito!")
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request,error)
                return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, 'update_password.html', {'form':form}) 
    else:
        messages.success(request, "No Autorizado")
        return redirect('home')


def delete_product(request, pk):
    if pk and request.method == "POST":
        product = Product.objects.get(id=pk)
        product.delete()
    return redirect('home')  


def update_product(request,pk):
    current_product = Product.objects.get(id=pk)
    form = UpdateProductForm(request.POST or None, request.FILES or None, instance=current_product)
    if request.method == "POST":
        form = UpdateProductForm(request.POST or None, request.FILES or None, instance=current_product)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado correctamente")
            return redirect('home')
        else:
            return render(request, 'update_product.html', {'product':current_product,'form':form}) 

    return render(request, 'update_product.html', {'product':current_product,'form':form}) 

def new_comment(request, product_id):
    product_comment = Product.objects.get(id=product_id)
    comment = Comment(product=product_comment, user = request.user)
    if request.method == "POST":
        comment_form = CommentForm(request.POST or None, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, "Comentario Publicado!")
            return redirect(request.META['HTTP_REFERER'])

def product(request, pk):
    product = Product.objects.get(id=pk)
    comment_list = Comment.objects.filter(product=product)
    comments_len = len(comment_list)
    if request.user.is_authenticated:
        comment = Comment(product=product, user = request.user)
    else:
        comment = Comment(product=product, user = None)
    comment.comment_content = ''
    comment_form = CommentForm(request.POST or None, instance=comment)
    return render(request, 'product.html', {'product':product, 'comments_len':comments_len, 'comments':comment_list, 'comment_form':comment_form})


def remove_comment(request, comment_id):
    if request.user.is_authenticated and request.user.is_staff:
        product_comment = Comment.objects.get(id=comment_id)
        product_comment.delete()
        messages.success(request, "Comentario Eliminado!")
        
    else:
        messages.error(request, "No Autorizado!")
    return redirect(request.META['HTTP_REFERER'])