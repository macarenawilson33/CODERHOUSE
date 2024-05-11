class Producto():
    def __init__(self, nombre, precio, codigo):
        self.name= nombre
        self.price= precio
        self.code= codigo   
    def __str__(self):
        return f"El precio del producto {self.name} es {self.price}"
        