import re
from datetime import date, timedelta
from employee.models import Employee

def validar_nombre(valor, campo):
    if not re.fullmatch(r'[A-Z]{1,20}', valor):
        raise ValueError(f"{campo} inválido: solo A-Z en mayúscula, sin acentos ni Ñ.")

def validar_otros_nombres(valor):
    if not re.fullmatch(r'[A-Z ]{1,50}', valor):
        raise ValueError("Otros Nombres inválido: solo letras mayúsculas y espacios.")

def validar_fecha_ingreso(fecha):
    hoy = date.today()
    if fecha > hoy:
        raise ValueError("La fecha de ingreso no puede ser futura.")
    if fecha < hoy - timedelta(days=31):
        raise ValueError("La fecha de ingreso no puede ser menor a un mes.")
    return fecha

def generar_correo_unico(nombre, apellido, pais):
    base_nombre = nombre.lower()
    base_apellido = re.sub(r'\s+', '', apellido.lower())
    dominio = 'cidenet.com.co' if pais == 'Colombia' else 'cidenet.com.us'
    base_email = f"{base_nombre}.{base_apellido}"

    empleados = Employee.objects.filter(email__startswith=base_email).order_by('email')
    usados = []

    for emp in empleados:
        local = emp.email.split('@')[0]
        if local.startswith(base_email + '.'):
            try:
                usados.append(int(local.split('.')[-1]))
            except:
                continue

    i = 0
    while i in usados:
        i += 1

    return f"{base_email}.{i}@{dominio}"
