class Usuario():
    
    def __init__ (self, nombre, apellido, correo_electronico, contrasena):
        self.name= nombre
        self.lastname= apellido
        self.email= correo_electronico
        self.password= contrasena
    
    def __str__ (self):
        return f"El usuario {self.name} {self.lastname} esta registrado con el siguiente correo electronico {self.email}"
    
    def valida_usuario (self, contrasena):
        return self.password == contrasena 
