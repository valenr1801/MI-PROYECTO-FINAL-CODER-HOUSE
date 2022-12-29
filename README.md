# MI-PROYECTO-FINAL-CODER-HOUSE
Proyecto Final- Ragaglia
Mi proyecto final
SEED DATA
Dentro de seed_data, encontramos nuestra base de datos original
 Para importar esta base de datos, debemos hacer:
   *python manage.py migrate
   *python manage.py runserver
   *python manage.py shell
   *python manage.py import seed_data
   Si nos aparecen los mensajes que dicen "todos las carreras, alumnos, y profesores de pruebas han sido cargados correctamente", está listo.

FORMS
Dentro del archivo forms , se encuentran los formularios según cada clase , en este caso, Carrerras, Alumnos y Profesores. A su vez, en el archivo base.html, encontramos todo los datos necesarios para no tener que repetir en todos los demás archivos el mismo código, y asi, poder optimizarlo.

URLS
Dentro de este archivo, encontramos todos los path o rutas que nos llevan a los sitios que requerimos.

MODELS
Dentro de models, tenemos definidas todas las clases principales de nuestro código.

VIEWS
Dentro de views, tenemos otras clases, que provienen de Forms y de clases padres.


- Ejemplo de MVT para la entrega final de Coder House Python, este codigo contiene:

Vistas
Formularios
Modelos
Templates

Importnante: Este ejemplo fue probado con python 3.7.10 y Django 4.1.3

1- Checkear que tengas Python

Para comenzar primero tienen que asegurarse que tienen instalado, Python.

En Windows tiene que abrir una terminal cmd o powershell.

PS C:\> python --version
Python 3.X.X 
En Linux/Mac tiene que abrir una terminal bash

$ python --version
Python 3.X.X 
Si les aparece la versión todo OK pueden seguir. Caso contrario descarguen Python.

2-Instalar Django

En una terminal cmd o powershell desde windows:

C:\> pip install django
Linux/Mac:

$ pip install django
Si no arrojo errores esto es suficiente para poder correr el projecto.

3-Instalar django bootstrap v5

C:\> pip install django-bootstrap-v5
Linux/Mac:

$ pip install django-bootstrap-v5
Clonar el projecto con git

windows:

C:\> git clone https://github.com/valenr1801/MI-PROYECTO-FINAL-CODER-HOUSE.git
Linux/Mac:

$ git clone https://github.com/valenr1801/MI-PROYECTO-FINAL-CODER-HOUSE.git
Luego, debemos correr el Servidor

Los siguientes comandos son análogos en Mac/Linux/Windows:

cd mi-primer-mvt
python manage.py migrate
La consola mostrara las migraciones de la base de datos que se realizaron.

Luego arrancamos el servidor web

python manage.py runserver
Listo ya tenes corriendo el ejemplo.

Ahora Hace click en el siguiente link para ver el ejemplo corriendo:

http://localhost:8000/


VIDEO YOUTUBE LINK: https://youtu.be/A7nEfdOxP0U
