from rest_framework import serializers
from employee.models import Employee
from employee.api.utils import generar_correo_unico, validar_nombre, validar_fecha_ingreso, validar_otros_nombres

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ['email', 'status', 'created_at']

    def validate(self, data):
        # Validaciones personalizadas
        validar_nombre(data['first_surname'], "Primer Apellido")
        validar_nombre(data['second_surname'], "Segundo Apellido")
        validar_nombre(data['first_name'], "Primer Nombre")

        if data.get('other_names'):
            validar_otros_nombres(data['other_names'])

        data['entry_date'] = validar_fecha_ingreso(data['entry_date'])

        return data

    def create(self, validated_data):
        correo = generar_correo_unico(validated_data['first_name'], validated_data['first_surname'],validated_data['country'])
        validated_data['email'] = correo
        return super().create(validated_data)