# core/models.py
from django.db import models
from django.contrib.auth.models import User

class Area(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Platillo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    areas = models.ManyToManyField(Area)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('En Preparación', 'En Preparación'),
        ('Listo', 'Listo'),
        ('Pagado', 'Pagado'),
        ('Cerrado', 'Cerrado'),
    ]

    mesa = models.CharField(max_length=10)
    mesero = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido {self.id} - Mesa {self.mesa}'

class Parte(models.Model):
    ESTADOS_PARTE = [
        ('Pendiente', 'Pendiente'),
        ('Preparando', 'Preparando'),
        ('Listo', 'Listo'),
        ('Completado', 'Completado'),
    ]

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='partes')
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS_PARTE, default='Pendiente')

    def __str__(self):
        return f'Parte {self.id} - {self.platillo.nombre} - {self.area.nombre}'
