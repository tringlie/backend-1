from django.db import models
from django.utils import timezone

class Dueno(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    ESTADOS = [('ACTIVO', 'Activo'), ('INACTIVO', 'Inactivo'), ('FALLECIDO', 'Fallecido')]
    
    dueno = models.ForeignKey(Dueno, on_delete=models.CASCADE, related_name='mascotas')
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2, help_text="Peso en kg")
    foto = models.ImageField(upload_to='mascotas/', blank=True, null=True)
    sexo = models.CharField(max_length=10, choices=[('M', 'Macho'), ('H', 'Hembra')])
    estado = models.CharField(max_length=20, choices=ESTADOS, default='ACTIVO')

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - {self.dueno.nombre}"

class Cita(models.Model):
    ESTADOS_CITA = [('PROGRAMADA', 'Programada'), ('COMPLETADA', 'Completada'), ('CANCELADA', 'Cancelada')]
    
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='citas')
    veterinario = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField()
    razon = models.CharField(max_length=200)
    estado = models.CharField(max_length=20, choices=ESTADOS_CITA, default='PROGRAMADA')
    notas = models.TextField(blank=True, null=True)
    duracion = models.IntegerField(help_text="Duración en minutos", default=30)

    def __str__(self):
        return f"Cita: {self.mascota.nombre} - {self.fecha_hora.strftime('%d/%m/%Y %H:%M')}"

class HistorialMedico(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='historiales')
    fecha = models.DateField(default=timezone.now)
    veterinario = models.CharField(max_length=100)
    diagnostico = models.TextField()
    tratamiento = models.TextField()

class Vacuna(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='vacunas')
    nombre = models.CharField(max_length=100)
    fecha_administracion = models.DateField()
    proximo_refuerzo = models.DateField(blank=True, null=True)
    veterinario = models.CharField(max_length=100)

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    presentacion = models.CharField(max_length=100)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, related_name='recetas')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT)
    dosis = models.CharField(max_length=100)
    duracion_dias = models.IntegerField()

class Factura(models.Model):
    cita = models.OneToOneField(Cita, on_delete=models.SET_NULL, null=True, blank=True)
    dueno = models.ForeignKey(Dueno, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    estado_pago = models.CharField(max_length=20, choices=[('PAGADO', 'Pagado'), ('PENDIENTE', 'Pendiente')], default='PENDIENTE')