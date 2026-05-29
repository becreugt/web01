from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('biblioteca/', include('biblioteca.urls')),

    # Permite entrar sin la diagonal final
    path('biblioteca', RedirectView.as_view(url='/biblioteca/', permanent=False)),
]