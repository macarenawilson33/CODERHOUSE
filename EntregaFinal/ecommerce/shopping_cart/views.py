from django.shortcuts import render, get_object_or_404
from .shopping_cart import ShoppingCart
from store.models import Product
from django.http import JsonResponse

# Create your views here.
def checkout(request):
    cart = ShoppingCart(request)
    cart_products = cart.get_cart_content()
    total_in_cart = 0.0
    for product in cart_products:
        total_in_cart=total_in_cart+float(product.price)
    return render(request, 'checkout.html', {'products':cart_products, 'cart_qty':len(cart_products), 'total_in_cart':total_in_cart})

def cart_add(request):
    cart = ShoppingCart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id = product_id)
        cart.add(product=product)

        cart_quantity = len(cart)
        #response = JsonResponse({'name':product.name, 'price':str(product.price)})
        response = JsonResponse({'cart_quantity':cart_quantity})
        return(response)


def cart_delete(request):
    cart = ShoppingCart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product = product_id)
        response = JsonResponse({'product':product_id})
        return(response)

def cart_update(request):
    pass
