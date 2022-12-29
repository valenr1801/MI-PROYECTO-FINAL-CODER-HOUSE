from django.shortcuts import render
from django.views.generic import ListView, CreateView , DetailView , DeleteView , UpdateView
from Educación_dos.models import Post , Mensaje
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.messages.views import SuccessMessageMixin
from Educación_dos.forms import UsuarioForm
from Educación_dos.models import Avatar , Post
from django.contrib.auth.admin import User

def index(request):
    post= Post.objects.order_by('-publicado_el').all()
    return render(request,"Educación_dos/index.html", {"posts": post})

class PostDetalle(DetailView):
    model=Post
   
class PostList(ListView):
    model= Post
    

class PostCrear(LoginRequiredMixin,CreateView):
    model= Post
    success_url= reverse_lazy("Educación-dos-listar")
    fields= '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model= Post
    success_url= reverse_lazy("Educación-dos-listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model= Post
    success_url= reverse_lazy("Educación-dos-listar")
    fields= '__all__'

class UserSignUp(CreateView):
    form_class= UsuarioForm
    template_name= 'registration/signup.html'
    success_url= reverse_lazy('Educación-dos-listar')

class UserLogin(LoginView):
    next_page= reverse_lazy("Educación-dos-listar")

class UserLogOut(LogoutView):
    next_page= reverse_lazy("Educación-dos-listar")

class AvatarActualizar(UpdateView):
    model= Avatar
    fields= ['imagen']
    success_url= reverse_lazy("Educación-dos-listar")

def AboutMe(request):
    return render(request,"Educación_dos/aboutme.html")

class UserActualizar(UpdateView):
    model=User
    fields= ['first_name', 'last_name', 'email']
    success_url= reverse_lazy("Educación-dos-listar")


class MensajeDetalle(LoginRequiredMixin, DetailView):
    model= Mensaje
   
class MensajeList(LoginRequiredMixin, ListView):
    model= Mensaje
    

class MensajeCrear(SuccessMessageMixin,CreateView):
    model= Mensaje
    fields= ['nombre', 'email', 'texto']
    success_url= reverse_lazy("Mensaje-crear")
    

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model= Mensaje
    success_url= reverse_lazy("Mensaje-listar")