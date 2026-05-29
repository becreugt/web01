from django.contrib import admin
from .models import Autor, Libro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    # Columnas que se verán en la lista de autores
    list_display = ('apellido', 'nombre', 'nacionalidad')
    # Permite buscar por nombre o apellido
    search_fields = ('nombre', 'apellido')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    # Columnas visibles en la lista de libros
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'isbn')
    # Filtro lateral por autor o fecha
    list_filter = ('autor', 'fecha_publicacion')
    # Buscador por título o ISBN
    search_fields = ('titulo', 'isbn')
    # Organiza la selección del autor con una interfaz de búsqueda (útil si tienes muchos)
    raw_id_fields = ('autor',)