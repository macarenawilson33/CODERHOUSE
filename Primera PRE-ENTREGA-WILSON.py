
usuarios = {}

def alta_usuario (nombre, contrasena):
    if nombre in usuarios:
        print (f"El usuario {nombre} ya existe")
    else:
        usuarios [nombre]= contrasena

def mostrar_informacion_usuarios ():
    for nombre in usuarios:
        contrasena= usuarios [nombre]
        print (f"la contraseña de {nombre} es {contrasena}")

def login_usuarios (nombre, contrasena):
    if nombre in usuarios:
        if usuarios [nombre]== contrasena:
            print("usuario valido")
        else:
            print ("contraseña invalida")    
    else:
        print ("usuario no encontrado")


while True:
    nombre_de_usuario= input("Ingrese su nombre:")
    if nombre_de_usuario == "":
        break
    contrasena_de_usuario= input ("Ingrese su contraseña:")
    alta_usuario(nombre_de_usuario,contrasena_de_usuario)


mostrar_informacion_usuarios()

nombre_de_usuario= input("Ingrese su nombre:")
contrasena_de_usuario= input ("Ingrese su contraseña:")
login_usuarios (nombre_de_usuario, contrasena_de_usuario)

