from django.contrib import admin
from django.urls import path, include  # <-- Asegúrate de importar 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    # Aquí incluyes el archivo urls.py de tu aplicación (asumiendo que tu app se llama 'biblioteca')
    path('biblioteca/', include('biblioteca.urls')), 
]