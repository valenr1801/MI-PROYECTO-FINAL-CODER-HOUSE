from Educación.models import Carreras, Alumnos, Profesores
#CARRERA
Carreras(nombre="Ingenieria en Sistemas", facultad="UTN", duracion= "6 años").save()
Carreras(nombre="Licenciatura en Economía", facultad="UNC-FCE", duracion="5 años").save()
Carreras(nombre="Medicina", facultad="UNC-FCM", duracion="5 años").save()
Carreras(nombre="Ingenieria Mecánica", facultad="UTN", duracion="6 años").save()
print("Se cargo con éxito las carreras de pruebas")

#ALUMNOS
Alumnos(nombre="Fabrizio", facultad="UTN", edad= "24 años").save()
Alumnos(nombre="Antonella", facultad="UNC-FCQ", edad= "18 años").save()
Alumnos(nombre="Valentina", facultad="UNC-FCE", edad= "21 años").save()
Alumnos(nombre="Delfina", facultad="UNC-FCQ", edad= "22 años").save()
print("Se cargo con éxito los alumnos de pruebas")

#PROFESORES
Profesores(nombre="Cristina", facultad="UNC-FCE", tiempo= "20 años").save()
Profesores(nombre="Ariel", facultad="UNC-FCE", tiempo= "22 años").save()
Profesores(nombre="Cecilia", facultad="UNC-FCE", tiempo= "18 años").save()
print("Se cargo con éxito los profesores de pruebas")