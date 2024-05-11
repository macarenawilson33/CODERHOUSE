from usuario import Usuario 
from producto import Producto

class Cliente (Usuario):   
    
    def __init__(self, nombre, apellido, correo_electronico, contrasena, codigo, domicilio, categoria):
        super().__init__(nombre, apellido, correo_electronico, contrasena)
        self.code= codigo
        self.address= domicilio
        self.category= categoria
        self.active= True
        self.shoppingcart= {}    
    
    def __str__(self):
        return (f"El código del cliente {self.name} {self.lastname} es {self.code} y su dirección es {self.address}")
    
    def agregar_producto_carrito (self, producto:Producto):
        self.shoppingcart [producto.code]= producto
    
    def vaciar_carrito (self):
        self.shoppingcart={}
        print("El carrito esta vacio")