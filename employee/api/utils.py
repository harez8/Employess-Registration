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
    #Eliminar espacios en el apellido compuesto
    base_nombre = nombre.lower()
    base_apellido = re.sub(r'\s+', '', apellido.lower())
    
    #Dominio segun el pais
    dominio = 'cidenet.com.co' if pais == 'Colombia' else 'cidenet.com.us'
    base_email = f"{base_nombre}.{base_apellido}"
    
    #Busca empleados cuyo correo comience con esa base
    empleados = Employee.objects.filter(email__startswith=base_email).order_by('email')
    usados = set()

    for emp in empleados:
        local = emp.email.split('@')[0]
        parts = local.split('.')
        
        #Si es exactamente base_email ocupa el 0
        if local == base_email:
            usados.add(0)
        elif len(parts) > 2 and parts[0] == base_nombre and parts[1] == base_apellido:
            try:
                usados.add(int(parts[2]))
            except ValueError:
                continue
            
    # Encontrar el menor número disponible
    i = 0
    while i in usados:
        i += 1
        
    correo = f"{base_email}.{i}@{dominio}" if i > 0 else f"{base_email}@{dominio}"
    if len(correo) > 300:
        raise ValueError("El correo generado supera los 300 caracteres.")

    return correo
