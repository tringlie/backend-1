from datetime import date
from decimal import Decimal

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


def migrar_mascotas_antiguas(apps, schema_editor):
    Mascota = apps.get_model('pacientes', 'Mascota')
    Dueno = apps.get_model('pacientes', 'Dueno')

    if not Mascota.objects.exists():
        return

    dueno_legacy, _ = Dueno.objects.get_or_create(
        email='migracion@local.invalid',
        defaults={
            'nombre': 'Dueño pendiente',
            'telefono': '',
            'direccion': '',
            'ciudad': '',
        },
    )

    hoy = date.today()

    for mascota in Mascota.objects.filter(dueno__isnull=True):
        edad = getattr(mascota, 'edad', None)

        if edad is not None and edad >= 0:
            anio_nacimiento = max(1900, hoy.year - edad)
        else:
            anio_nacimiento = 2000

        mascota.dueno = dueno_legacy
        mascota.fecha_nacimiento = date(anio_nacimiento, 1, 1)
        mascota.peso = Decimal('0.00')
        mascota.sexo = ''

        mascota.save(
            update_fields=[
                'dueno',
                'fecha_nacimiento',
                'peso',
                'sexo',
            ]
        )


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dueno',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=100)),
            ],
        ),

        migrations.AddField(
            model_name='mascota',
            name='dueno',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='mascotas',
                to='pacientes.dueno',
            ),
        ),

        migrations.AddField(
            model_name='mascota',
            name='raza',
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
            ),
        ),

        migrations.AddField(
            model_name='mascota',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),

        migrations.AddField(
            model_name='mascota',
            name='peso',
            field=models.DecimalField(
                decimal_places=2,
                help_text='Peso en kg',
                max_digits=5,
                null=True,
            ),
        ),

        migrations.AddField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='mascotas/',
            ),
        ),

        migrations.AddField(
            model_name='mascota',
            name='sexo',
            field=models.CharField(
                choices=[
                    ('M', 'Macho'),
                    ('H', 'Hembra'),
                ],
                max_length=10,
                null=True,
            ),
        ),

        migrations.AddField(
            model_name='mascota',
            name='estado',
            field=models.CharField(
                choices=[
                    ('ACTIVO', 'Activo'),
                    ('INACTIVO', 'Inactivo'),
                    ('FALLECIDO', 'Fallecido'),
                ],
                default='ACTIVO',
                max_length=20,
            ),
        ),

        migrations.RunPython(
            migrar_mascotas_antiguas,
            migrations.RunPython.noop,
        ),

        migrations.AlterField(
            model_name='mascota',
            name='dueno',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='mascotas',
                to='pacientes.dueno',
            ),
        ),

        migrations.AlterField(
            model_name='mascota',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),

        migrations.AlterField(
            model_name='mascota',
            name='peso',
            field=models.DecimalField(
                decimal_places=2,
                help_text='Peso en kg',
                max_digits=5,
            ),
        ),

        migrations.AlterField(
            model_name='mascota',
            name='sexo',
            field=models.CharField(
                choices=[
                    ('M', 'Macho'),
                    ('H', 'Hembra'),
                ],
                max_length=10,
            ),
        ),

        migrations.RemoveField(
            model_name='mascota',
            name='edad',
        ),

        migrations.RemoveField(
            model_name='mascota',
            name='vacunacion',
        ),

        migrations.AlterModelOptions(
            name='mascota',
            options={},
        ),

        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('veterinario', models.CharField(max_length=100)),
                ('fecha_hora', models.DateTimeField()),
                ('razon', models.CharField(max_length=200)),
                ('estado', models.CharField(
                    choices=[
                        ('PROGRAMADA', 'Programada'),
                        ('COMPLETADA', 'Completada'),
                        ('CANCELADA', 'Cancelada'),
                    ],
                    default='PROGRAMADA',
                    max_length=20,
                )),
                ('notas', models.TextField(blank=True, null=True)),
                ('duracion', models.IntegerField(
                    default=30,
                    help_text='Duración en minutos',
                )),
                ('mascota', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='citas',
                    to='pacientes.mascota',
                )),
            ],
        ),

        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('nombre', models.CharField(max_length=100)),
                ('presentacion', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('precio', models.DecimalField(
                    decimal_places=2,
                    max_digits=10,
                )),
                ('fecha_vencimiento', models.DateField()),
            ],
        ),

        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_administracion', models.DateField()),
                ('proximo_refuerzo', models.DateField(
                    blank=True,
                    null=True,
                )),
                ('veterinario', models.CharField(max_length=100)),
                ('mascota', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='vacunas',
                    to='pacientes.mascota',
                )),
            ],
        ),

        migrations.CreateModel(
            name='HistorialMedico',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('fecha', models.DateField(
                    default=django.utils.timezone.now,
                )),
                ('veterinario', models.CharField(max_length=100)),
                ('diagnostico', models.TextField()),
                ('tratamiento', models.TextField()),
                ('mascota', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='historiales',
                    to='pacientes.mascota',
                )),
            ],
        ),

        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('dosis', models.CharField(max_length=100)),
                ('duracion_dias', models.IntegerField()),
                ('cita', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='recetas',
                    to='pacientes.cita',
                )),
                ('medicamento', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    to='pacientes.medicamento',
                )),
            ],
        ),

        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('monto', models.DecimalField(
                    decimal_places=2,
                    max_digits=10,
                )),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('estado_pago', models.CharField(
                    choices=[
                        ('PAGADO', 'Pagado'),
                        ('PENDIENTE', 'Pendiente'),
                    ],
                    default='PENDIENTE',
                    max_length=20,
                )),
                ('cita', models.OneToOneField(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    to='pacientes.cita',
                )),
                ('dueno', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='pacientes.dueno',
                )),
            ],
        ),
    ]