"""MiProyectoFinalCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Educación.views import (mostrar_carreras, mostrar_alumnos, BuscarAlumnos, BuscarCarreras, AltaCarreras , AltaAlumnos, ActualizarCarreras, ActualizarAlumnos, CarrerasDetalle, CarrerasList,
                             CarrerasCrear, CarrerasBorrar, CarrerasActualizar,AlumnosDetalle, AlumnosList,
                             AlumnosCrear, AlumnosBorrar, AlumnosActualizar, ProfesoresDetalle, ProfesoresList,
                             ProfesoresCrear, ProfesoresBorrar, ProfesoresActualizar)
from Educación_dos.views import (index , PostList , PostCrear , PostBorrar , PostActualizar, PostDetalle, 
                                 UserSignUp, UserLogin, UserLogOut, AvatarActualizar, AboutMe, UserActualizar, MensajeCrear, MensajeList, MensajeDetalle)

from Educación_dos import views

urlpatterns = [
      path('admin/', admin.site.urls),
      path('panel-carreras/<int:pk>/detalle', CarrerasDetalle.as_view()),
      path('panel-carreras/', CarrerasList.as_view()),
      path('panel-carreras/crear', CarrerasCrear.as_view()),
      path('panel-carreras/<int:pk>/borrar', CarrerasBorrar.as_view()),
      path('panel-carreras/<int:pk>/actualizar', CarrerasActualizar.as_view()),
      path('panel-alumnos/<int:pk>/detalle', AlumnosDetalle.as_view()),
      path('panel-alumnos/', AlumnosList.as_view()),
      path('panel-alumnos/crear', AlumnosCrear.as_view()),
      path('panel-alumnos/<int:pk>/borrar', AlumnosBorrar.as_view()),
      path('panel-alumnos/<int:pk>/actualizar', AlumnosActualizar.as_view()),
      path('panel-profesores/<int:pk>/detalle', ProfesoresDetalle.as_view()),
      path('panel-profesores/', ProfesoresList.as_view()),
      path('panel-profesores/crear', ProfesoresCrear.as_view()),
      path('panel-profesores/<int:pk>/borrar', ProfesoresBorrar.as_view()),
      path('panel-profesores/<int:pk>/actualizar', ProfesoresActualizar.as_view()),
      path('Educación-dos/',index, name= "Educación-dos-index"),
      path('Educación-dos/<int:pk>/detalle',PostDetalle.as_view(), name= "Educación-dos-detalle"),
      path('Educación-dos/listar',PostList.as_view(), name= "Educación-dos-listar"), 
      path('Educación-dos/crear',PostCrear.as_view(), name= "Educación-dos-crear"), 
      path('Educación-dos/<int:pk>/actualizar',PostActualizar.as_view(), name= "Educación-dos-actualizar"), 
      path('Educación-dos/<int:pk>/borrar',PostBorrar.as_view(), name= "Educación-dos-borrar"), 
      path('Educación-dos/signup',UserSignUp.as_view(), name= "Educación-dos-signup"),
      path('Educación-dos/login',UserLogin.as_view(), name= "Educación-dos-login"), 
      path('Educación-dos/logout',UserLogOut.as_view(), name= "Educación-dos-logout"), 
      path('Educación-dos/avatar/<int:pk>/actualizar',AvatarActualizar.as_view(), name= "Avatar-actualizar"), 
      path('Aboutme/', views.AboutMe, name="Sobremi"),
      path('Mensajes/<int:pk>/listar',MensajeList.as_view(), name= "Mensaje-listar"), 
      path('Mensaje/<int:pk>/detalle',MensajeDetalle.as_view(), name= "Mensaje-detalle"), 
      path('Mensaje/crear',MensajeCrear.as_view(), name= "Mensaje-crear"), 
      path('Educación_dos/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="Usuario-actualizar"),
  ]
  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)