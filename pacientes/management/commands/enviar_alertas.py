# pacientes/management/commands/enviar_alertas.py
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from pacientes.models import Cita, Vacuna

class Command(BaseCommand):
    help = 'Envía alertas por correo de citas próximas (24h) y refuerzos de vacunas'

    def handle(self, *args, **kwargs):
        hoy = timezone.localtime()
        manana = hoy + timedelta(days=1)
        
        # 1. Alerta: Cita en 24 horas
        citas_manana = Cita.objects.filter(
            fecha_hora__date=manana.date(),
            estado='PROGRAMADA'
        )
        
        for cita in citas_manana:
            dueno = cita.mascota.dueno
            asunto = f"Recordatorio de Cita - {cita.mascota.nombre}"
            mensaje = (
                f"Hola {dueno.nombre},\n\nLe recordamos que {cita.mascota.nombre} "
                f"tiene una cita programada para mañana a las {cita.fecha_hora.strftime('%H:%M')}.\n"
                f"Motivo: {cita.razon}\n\n¡Los esperamos!"
            )
            send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, [dueno.email], fail_silently=False)
            self.stdout.write(self.style.SUCCESS(f'Cita 24h enviada a {dueno.email}'))

        # 2. Alerta: Próximo refuerzo (avisa con 7 días de anticipación)
        en_siete_dias = hoy.date() + timedelta(days=7)
        vacunas_proximas = Vacuna.objects.filter(proximo_refuerzo=en_siete_dias)

        for vacuna in vacunas_proximas:
            dueno = vacuna.mascota.dueno
            asunto = f"Próximo refuerzo de vacuna para {vacuna.mascota.nombre}"
            mensaje = (
                f"Hola {dueno.nombre},\n\nLe recordamos que el {vacuna.proximo_refuerzo.strftime('%d/%m/%Y')} "
                f"le corresponde el refuerzo de la vacuna '{vacuna.nombre}' a {vacuna.mascota.nombre}.\n\n"
                f"Por favor, agende una cita con nosotros.\n\nSaludos cordiales."
            )
            send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, [dueno.email], fail_silently=False)
            self.stdout.write(self.style.SUCCESS(f'Alerta vacuna enviada a {dueno.email}'))

        self.stdout.write(self.style.SUCCESS('\nProceso de alertas automáticas finalizado.'))