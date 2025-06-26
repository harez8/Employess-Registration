from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class Employee(models.Model):
    COUNTRY_CHOICES = [
        ('Colombia', 'Colombia'),
        ('Estados Unidos', 'Estados Unidos'),
    ]

    AREA_CHOICES = [
        ('Administración', 'Administración'),
        ('Financiera', 'Financiera'),
        ('Compras', 'Compras'),
        ('Infraestructura', 'Infraestructura'),
        ('Operación', 'Operación'),
        ('Talento Humano', 'Talento Humano'),
        ('Servicios Varios', 'Servicios Varios'),
    ]

    id = models.AutoField(primary_key=True)
    first_surname = models.CharField(max_length=20)
    second_surname = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    other_names = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES)
    id_type = models.CharField(max_length=30)
    id_number = models.CharField(max_length=20)
    email = models.CharField(max_length=300, unique=True)
    entry_date = models.DateField()
    area = models.CharField(max_length=50, choices=AREA_CHOICES)
    status = models.CharField(max_length=10, default='Activo', editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        unique_together = ('id_type', 'id_number')

    def __str__(self):
        return f"{self.first_name} {self.first_surname}"