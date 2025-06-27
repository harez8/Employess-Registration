# Employess-Registration

# Registro de Empleados - Cidenet

Este es un sistema desarrollado como prueba técnica para la empresa **Cidenet S.A.S.**, cuyo objetivo es permitir el registro de empleados con validaciones específicas y generación automática de correos electrónicos institucionales.

## Estructura del proyecto

Employess-Registration/
├── employee_r/ # Proyecto principal Django

│ ├── employee/ # Aplicación que contiene los modelos y lógica

│ ├── employee_r/ # Configuración del proyecto Django

│ ├── db_scripts.sql # Scripts SQL exportados

│ ├── manage.py # Comando principal

│ └── requirements.txt # Dependencias del proyecto

└── README.md 


---
## Validaciones implementadas

- Validación de campos en mayúsculas (sin acentos ni Ñ)
- Validación de longitud y caracteres permitidos
- Validación de fecha de ingreso (hasta 1 mes anterior y no mayor a hoy)
- Generación automática y única de correo institucional:
  - Formato: primer_nombre.primer_apellido@dominio
  - Dominio según el país (Colombia o EE. UU.)
  - Secuencial si ya existe (ej. juan.perez.2@cidenet.com.co)
- Estado inicial del empleado siempre es "ACTIVO"
- Fecha y hora de registro automática

---

## Tecnologías utilizadas

- Python 3.10+
- Django 4.2
- Django REST Framework
- MySQL
- 'mysqlclient' (conector)
- Git

---

## Requisitos previos

1. Tener Python 3 instalado.
2. Tener MySQL instalado y ejecutándose.
3. Crear una base de datos en MySQL (por ejemplo, 'bd_employees').
4. Crear un usuario MySQL con permisos (o usar 'root' si lo prefieres).
5. Clonar este repositorio:

   git clone https://github.com/harez8/Employess-Registration.git
   cd employee_r
---
## Configuracion del entorno

1. Crear el entorno virtual e instalar dependencias:
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt

2. Configurar la base de datos:
    Editar 'settings.py'  

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'nombre_bd', <-----
        'USER': 'usuario', <-----
        'PASSWORD': 'contraseña', <-----
        'HOST': 'localhost', <-----
        'PORT': '3306', <-----
    } 
}

3.Generacion de Sripts de la base de datos
    python manage.py sqlmigrate employee 0001 > db_scripts.sql

4. Aplicar migraciones:
    python manage.py makemigrations
    python manage.py migrate

5. Ejecutar el servidor: 
    python manage.py runserver

La API estara disponible en: http://127.0.0.1:8000/api/employees/

---

 ## Endpoints disponibles

POST /api/employees/ → Registrar nuevo empleado

GET /api/employees/ → Ver lista de empleados

---

## Pruebas con Postman

Puedes usar Postman para enviar solicitudes a la API:

**POST** 'http://127.0.0.1:8000/api/employees/'

Ejemplo de cuerpo de solicitud (JSON):

```json
{
  "first_surname": "PEREZ",
  "second_surname": "GOMEZ",
  "first_name": "JUAN",
  "other_names": "CARLOS",
  "country": "Colombia",
  "id_type": "Cedula de ciudadania",
  "id_number": "123456789",
  "entry_date": "2025-06-01",
  "area": "Talento Humano"
  "status": "Activo",
  "created_at": "2025-06-26T17:51:09.124221Z"
}

Desarrollado por **Heider Restrepo Z.** como parte del proceso de selección para Cidenet S.A.S.  
