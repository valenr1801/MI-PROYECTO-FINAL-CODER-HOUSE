from django.shortcuts import render , get_object_or_404
from Educación.models import Carreras , Alumnos , Profesores
from Educación.forms import Buscar , CarrerasForm , AlumnosForm , ProfesoresForm
from django.views import View  
from django.views.generic import DetailView , ListView , CreateView , DeleteView , UpdateView

def mostrar_carreras(request):
  lista_carreras = Carreras.objects.all()
  return render(request, "carreras.html", {"lista_carreras": lista_carreras})

class BuscarCarreras(View):
    form_class = Buscar
    template_name = 'buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_carreras = Carreras.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_carreras':lista_carreras})
        return render(request, self.template_name, {"form": form})

class AltaCarreras(View):

    form_class = CarrerasForm
    template_name = 'alta_carreras.html'
    initial = {"nombre":"", "facultad":"", "duracion":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargo con éxito la carrera {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarCarreras(View):
  form_class = CarrerasForm
  template_name = 'actualizar_carreras.html'
  initial = {"nombre":"", "facultad":"", "duracion":""}
  
  
  def get(self, request, pk): 
      carrera= get_object_or_404(Carreras, pk=pk)
      form = self.form_class(instance=carrera)
      return render(request, self.template_name, {'form':form,'carrera': carrera})

  
  def post(self, request, pk): 
      carrera = get_object_or_404(carrera, pk=pk)
      form = self.form_class(request.POST ,instance=carrera)
      if form.is_valid():
          form.save()
          msg_exito = f"Se actualizó con éxito la carrera {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'carrera': carrera,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

#CRUD
class CarrerasDetalle(DetailView):
  model = Carreras
  template_name= 'carreras_detail.html'
  success_url= "/panel-carreras/detalle/"
  fields = ["nombre", "facultad", "duracion"]

class CarrerasList(ListView):
  model = Carreras
  template_name= 'carreras_list.html'
  success_url="/panel-carreras/"
  fields = ["nombre", "facultad", "duracion"]

class CarrerasCrear(CreateView):
  model = Carreras
  success_url = "/panel-carreras/"
  template_name= 'carreras_form.html'
  fields = ["nombre", "facultad", "duracion"]

class CarrerasBorrar(DeleteView):
  model = Carreras
  success_url = "/panel-carreras/"
  template_name= 'carreras_confirm_delete.html'

class CarrerasActualizar(UpdateView):
  model= Carreras
  template_name= 'carreras_form.html'
  success_url = "/panel-carreras/"
  fields = ["nombre", "facultad", "duracion"]

  #ALUMNOS
def mostrar_alumnos(request):
   lista_alumnos = Alumnos.objects.all()
   return render(request, "alumnos.html", {"lista_alumnos": lista_alumnos})

class BuscarAlumnos(View):
    form_class = Buscar
    template_name = 'buscar_alumnos.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_alumnos = Alumnos.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_alumnos':lista_alumnos})
        return render(request, self.template_name, {"form": form})

class AltaAlumnos(View):

    form_class = AlumnosForm
    template_name = 'alta_alumnos.html'
    initial = {"nombre":"", "facultad":"", "edad":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargo con éxito el alumno {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarAlumnos(View):
  form_class = AlumnosForm
  template_name = 'actualizar_alumnos.html'
  initial = {"nombre":"", "facultad":"", "edad":""}
  
  
  def get(self, request, pk): 
      alumno= get_object_or_404(Alumnos, pk=pk)
      form = self.form_class(instance=alumno)
      return render(request, self.template_name, {'form':form,'alumno': alumno})

  
  def post(self, request, pk): 
      alumno = get_object_or_404(Alumnos, pk=pk)
      form = self.form_class(request.POST ,instance=alumno)
      if form.is_valid():
          form.save()
          msg_exito = f"Se actualizó con éxito el alumno {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'alumno': alumno,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})


#CRUD
class AlumnosDetalle(DetailView):
  model = Alumnos
  template_name= 'alumnos_detail.html'
  success_url= "/panel-alumnos/detalle/"
  fields = ["nombre", "facultad", "edad"]
  
class AlumnosList(ListView):
  model = Alumnos
  template_name= 'alumnos_list.html'
  success_url="/panel-alumnos/"
  fields = ["nombre", "facultad", "edad"]

class AlumnosCrear(CreateView):
  model = Alumnos
  success_url = "/panel-alumnos/"
  template_name= 'alumnos_form.html'
  fields = ["nombre", "facultad", "edad"]

class AlumnosBorrar(DeleteView):
  model = Alumnos
  success_url = "/panel-alumnos/"
  template_name= 'alumnos_confirm_delete.html'

class AlumnosActualizar(UpdateView):
  model= Alumnos
  template_name= 'alumnos_form.html'
  success_url = "/panel-alumnos/"
  fields = ["nombre", "facultad", "edad"]

#CRUD
class ProfesoresDetalle(DetailView):
  model = Profesores
  template_name= 'profesores_detail.html'
  success_url= "/panel-profesores/detalle/"
  fields = ["nombre", "facultad", "tiempo"]
  
class ProfesoresList(ListView):
  model = Profesores
  template_name= 'profesores_list.html'
  success_url="/panel-profesores/"
  fields = ["nombre", "facultad", "tiempo"]

class ProfesoresCrear(CreateView):
  model = Profesores
  success_url = "/panel-profesores/"
  template_name= 'profesores_form.html'
  fields = ["nombre", "facultad", "tiempo"]

class ProfesoresBorrar(DeleteView):
  model = Profesores
  success_url = "/panel-profesores/"
  template_name= 'profesores_confirm_delete.html'

class ProfesoresActualizar(UpdateView):
  model= Profesores
  template_name= 'succes_updated_message'
  success_url = "/panel-profesores/"
  fields = ["nombre", "facultad", "tiempo"]
