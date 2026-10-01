from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Delega la ruta /mascotas/ al archivo urls.py de la app pacientes
    path('mascotas/', include('pacientes.urls')),
]

# Configuración para que Django pueda mostrar las fotos (Pillow) en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)