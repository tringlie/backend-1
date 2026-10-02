from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

# Importamos la vista personalizada
from pacientes.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Usamos CustomLoginView pero mantenemos la ruta original de tu template
    path(
        'login/',
        CustomLoginView.as_view(
            template_name='registration/login.html'
        ),
        name='login',
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(
            next_page='login'
        ),
        name='logout',
    ),

    path(
        'pacientes/',
        include('pacientes.urls'),
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )