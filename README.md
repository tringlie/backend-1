# backend-1
evaluacion 1 backend

## Caso 5: Sistema de Pacientes para Clínica Veterinaria


GUIA CHATGPT PARA EL TRABAJO

# 🐾 Sistema de Pacientes - Clínica Veterinaria (Caso 5)

Sistema web en **Django 4.2** para el control y estado de vacunación de pacientes veterinarios.

---

## 🚀 Inicio Rápido (Windows + VSCode)

### 1. Clonar y abrir el proyecto
Abre la terminal de VSCode (`Ctrl + ñ` o `Ctrl + \``) y ejecuta:
```powershell
git clone [https://github.com/tringlie/backend-1](https://github.com/tringlie/backend-1)
cd TU_REPOSITORIO
code .

2. Crear y activar el entorno virtual
PowerShell

# Crear entorno
python -m venv venv

# Habilitar permisos (solo si PowerShell da error de scripts)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Activar entorno
.\venv\Scripts\Activate.ps1

(Debe aparecer (venv) al inicio de tu terminal).

    Tip VSCode: Presiona Ctrl + Shift + P > Python: Select Interpreter > Selecciona .\venv\Scripts\python.exe.

3. Instalar dependencias
PowerShell

pip install -r requisitos.txt

4. Configurar base de datos y administrador
PowerShell

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

5. Iniciar servidor
PowerShell

python manage.py runserver

    Panel de Administración: http://127.0.0.1:8000/admin/ (Cargar mínimo 5 mascotas)

    Listado de Pacientes: http://127.0.0.1:8000/mascotas/

🌿 Flujo de Trabajo en Git

    Actualizar main: git pull origin main

    Crear rama: git checkout -b feature/mi-tarea

    Guardar cambios:
    PowerShell

    git add .
    git commit -m "Descripción clara del cambio"
    git push origin feature/mi-tarea

    Pull Request: Abrir PR en GitHub hacia main para revisión del equipo.