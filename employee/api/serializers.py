from rest_framework import serializers
from employee.models import Employee
from employee.api.utils import generar_correo_unico, validar_nombre, validar_fecha_ingreso, validar_otros_nombres

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ['email', 'status', 'created_at']

    def validate(self, data):
        # Asegura mayúsculas antes de validar
        for field in ['first_name', 'first_surname', 'second_surname', 'other_names']:
            valor = data.get(field)
            if valor:
                data[field] = valor.upper().strip()
            
        # Validaciones personalizadas
        validar_nombre(data['first_surname'], "Primer Apellido")
        validar_nombre(data['second_surname'], "Segundo Apellido")
        validar_nombre(data['first_name'], "Primer Nombre")

        if data.get('other_names'):
            validar_otros_nombres(data['other_names'])

        data['entry_date'] = validar_fecha_ingreso(data['entry_date'])

        return data

    def create(self, validated_data):
        # Generar correo primero con los datos validados (no del objeto aún)
        correo = generar_correo_unico(
            nombre=validated_data['first_name'],
            apellido=validated_data['first_surname'],
            pais=validated_data['country']
    )
        
        validated_data['email'] = correo
        validated_data['status'] = 'ACTIVO'
        
        return Employee.objects.create(**validated_data)