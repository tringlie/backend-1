# backend-1

Evaluación 1 - Programación Back End

## 🐾 Caso 5: Sistema de Pacientes para Clínica Veterinaria

Sistema web desarrollado con **Django 4.2** para el registro y control del estado de vacunación de pacientes veterinarios.

---

## 🚀 Inicio rápido

### 1. Clonar y abrir el proyecto

```bash
git clone https://github.com/tringlie/backend-1.git
cd backend-1
code .
```

### 2. Crear y activar el entorno virtual

#### Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

#### Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Cuando el entorno esté activo debería aparecer `(venv)` al inicio de la terminal.

### 3. Instalar dependencias

```bash
pip install -r requisitos.txt
```

El proyecto utiliza **Django 4.2.19**.

### 4. Configurar la base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear administrador

```bash
python manage.py createsuperuser
```

Desde Django Admin se deben cargar como mínimo **5 mascotas**.

### 6. Iniciar servidor

```bash
python manage.py runserver
```

Panel de Administración:

http://127.0.0.1:8000/admin/

Listado de Pacientes:

http://127.0.0.1:8000/pacientes/

---

## 🐶 Funcionalidades

El sistema permite:

- Listar todas las mascotas registradas.
- Buscar mascotas por nombre.
- Filtrar mascotas por especie.
- Filtrar mascotas según su estado de vacunación.
- Ver rápidamente las mascotas con vacunación pendiente.
- Mostrar el estado de vacunación mediante colores:
  - Verde: Al día.
  - Rojo: Pendiente.
  - Amarillo: Alergia.
- Crear y editar mascotas mediante Django Admin.
- Actualizar el estado de vacunación desde Django Admin.

---

## 📋 Modelo Mascota

Cada mascota registra cuatro datos principales:

```text
Mascota
├── nombre
├── especie
├── edad
└── vacunación
```

Estados de vacunación disponibles:

```text
Al día
Pendiente
Alergia
```

---

## 🌿 Flujo de trabajo en Git

Actualizar `main`:

```bash
git switch main
git pull origin main
```

Crear una rama:

```bash
git switch -c nombre-rama
```

Guardar cambios:

```bash
git add .
git commit -m "Descripción clara del cambio"
```

Subir la rama:

```bash
git push -u origin nombre-rama
```

Luego abrir un **Pull Request hacia `main`** para revisión antes de integrar los cambios.
