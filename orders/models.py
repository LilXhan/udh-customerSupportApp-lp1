from django.db import models

from users.models import User
from django.db.models import SET_NULL

class Order(models.Model):
    estados = (
        ('pendiente', 'Pendiente'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado')
    )

    titulo = models.CharField(max_length=25, null=True)
    creado_el = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(max_length=255)
    total = models.FloatField()
    estado = models.CharField(max_length=20, choices=estados, default='pendiente')
    usuario = models.ForeignKey(User, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.titulo