from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

# Importamos la vista personalizada de login que creamos en views.py
from pacientes.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Usamos CustomLoginView en lugar de auth_views.LoginView
    path(
        'login/',
        CustomLoginView.as_view(),
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