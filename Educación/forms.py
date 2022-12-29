from django import forms
from Educación.models import Carreras , Alumnos , Profesores

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

class CarrerasForm(forms.ModelForm):
  class Meta:
    model = Carreras
    fields = ['nombre', 'facultad', 'duracion']

class AlumnosForm(forms.ModelForm):
  class Meta:
    model = Alumnos
    fields = ['nombre', 'facultad', 'edad']

class ProfesoresForm(forms.ModelForm):
  class Meta:
    model = Profesores
    fields = ['nombre', 'facultad', 'tiempo']