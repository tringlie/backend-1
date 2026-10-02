# pacientes/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Receta

@receiver(post_save, sender=Receta)
def enviar_alerta_receta(sender, instance, created, **kwargs):
    # 'created' es True solo cuando la receta se crea por primera vez
    if created:
        # Extraemos el dueño navegando por las relaciones ForeignKey
        dueno = instance.cita.mascota.dueno
        
        asunto = f"Receta lista para {instance.cita.mascota.nombre}"
        mensaje = (
            f"Hola {dueno.nombre},\n\n"
            f"La receta médica de {instance.cita.mascota.nombre} ya está disponible.\n\n"
            f"Medicamento: {instance.medicamento.nombre}\n"
            f"Dosis: {instance.dosis}\n"
            f"Duración: {instance.duracion_dias} días\n\n"
            f"Saludos cordiales,\nClínica Veterinaria"
        )
        
        send_mail(
            asunto, 
            mensaje, 
            settings.EMAIL_HOST_USER, 
            [dueno.email], 
            fail_silently=True # Si falla (ej. sin internet), no rompe la página
        )