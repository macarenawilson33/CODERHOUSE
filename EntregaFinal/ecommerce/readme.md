Instalacion y ejecucion:
1.- Dejar los archivos en un directorio de trabajo
2.- En el mismo nivel del directorio "ecommerce" ejecutar "pipenv install" (pipenv es la manera que se eligio para crear y activar el virtual env, se pueden usar otros metodos de asi desearlo)
3.- Activar el virtual environment con "pipenv shell"
4.- Installar pillow con "pip install django"
5.- Installar pillow con "pip install pillow"
6.- Ingresar por linea de comandos a la carpeta "ecommerce" y ejecutar "python manage.py runserver"

Secciones y funcionalidades
1.-	Clickeando sobre Macus Shop usted podrá dirigirse a la página de inicio, sin importar en que sección se encuentre. Lo mismo sucederá al presionar Inicio.
2.-	El sistema cuenta con las siguientes secciones About, Tienda, Acceder, Registrarse y Carrito, cuyas funcionalidades serán brevemente comentadas a continuación: 
3.-	En la sección About, podrá leer un breve comentario acerca de la autora.
4.-	Al clickear en Tienda se despliegan las siguientes opciones: Todos los productos (donde se pueden ver la totalidad de los productos de la página), Libros, Vinilos y Comics (pudiendo ingresar a los productos según su tipo)
5.-	En Acceder se habilita el ingreso a usuarios registrados, mientras que en Registrarse se dará la opción de crear un usuario nuevo.  
6.-	En la Sección Carrito se pueden observar los productos agregados al carrito.
7.-	Cada producto además cuenta con una sección de comentarios, la cual solo estará habilitada para usuarios registrados. 
8.-	Los usuarios con permisos de Admin además podrán cargar productos nuevos, modificar los ya cargados y eliminarlos.  

La instalacion incluye:
-> 9 productos de prueba, 3 de cada tipo.
-> Usuario administrador: admin , password: admin (cambiar antes de publicar).
-> Usuario Cliente: pepe , password: Ramiro123 (cambiar o eliminar antes de publicar).