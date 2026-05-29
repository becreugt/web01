from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Autor, Libro

def inicio(request):
    return render(request, 'biblioteca/inicio.html')

# ==============================================================================
# VISTAS PARA EL MODELO AUTOR
# ==============================================================================

class AutorListView(ListView):
    model = Autor
    template_name = 'autor_list.html'  # Especifica tu plantilla
    context_object_name = 'autores'              # Nombre de la variable en el HTML

class AutorDetailView(DetailView):
    model = Autor
    template_name = 'biblioteca/autor_detail.html'
    context_object_name = 'autor'

class AutorCreateView(CreateView):
    model = Autor
    fields = ['nombre', 'apellido', 'nacionalidad', 'fecha_nacimiento']
    template_name = 'biblioteca/autor_form.html'
    success_url = reverse_lazy('autor_list')     # Redirige a la lista al guardar

class AutorUpdateView(UpdateView):
    model = Autor
    fields = ['nombre', 'apellido', 'nacionalidad', 'fecha_nacimiento']
    template_name = 'biblioteca/autor_form.html' # Reutiliza la misma plantilla de creación
    success_url = reverse_lazy('autor_list')

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'biblioteca/autor_confirm_delete.html'
    success_url = reverse_lazy('autor_list')


# ==============================================================================
# VISTAS PARA EL MODELO LIBRO
# ==============================================================================

class LibroListView(ListView):
    model = Libro
    template_name = 'biblioteca/libro_list.html'
    context_object_name = 'libros'
    
    # Opcional: Optimiza la consulta cargando el autor para evitar el problema de N+1 consultas
    def get_queryset(self):
        return Libro.objects.select_related('autor').all()

class LibroDetailView(DetailView):
    model = Libro
    template_name = 'biblioteca/libro_detail.html'
    context_object_name = 'libro'

class LibroCreateView(CreateView):
    model = Libro
    fields = ['titulo', 'isbn', 'fecha_publicacion', 'paginas', 'autor', 'resumen']
    template_name = 'biblioteca/libro_form.html'
    success_url = reverse_lazy('libro_list')

class LibroUpdateView(UpdateView):
    model = Libro
    fields = ['titulo', 'isbn', 'fecha_publicacion', 'paginas', 'autor', 'resumen']
    template_name = 'biblioteca/libro_form.html'
    success_url = reverse_lazy('libro_list')

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'biblioteca/libro_confirm_delete.html'
    success_url = reverse_lazy('libro_list')