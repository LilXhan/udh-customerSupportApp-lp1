from django.db import models
from django.db.models import SET_NULL

from users.models import User
from comments.models import Comment
from orders.models import Order

class Ticket(models.Model):
    asunto = models.CharField(max_length=255)
    descripcion = models.TextField()
    canal = models.CharField(max_length=255)
    grupo = models.CharField(max_length=255)
    creado_el = models.DateTimeField(auto_now_add=True)
    actualizado_el = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=100, default='New')
    usuario = models.ForeignKey(User, on_delete=SET_NULL, null=True, related_name='usuario_user')
    agente = models.ForeignKey(User, on_delete=SET_NULL, null=True, related_name='agente_user')
    comentario = models.ForeignKey(Comment, on_delete=SET_NULL, null=True)
    pedido = models.ForeignKey(Order, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.asunto