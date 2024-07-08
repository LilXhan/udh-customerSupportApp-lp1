from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Comment(models.Model):
    titulo = models.CharField(max_length=20, null=True)
    creado_el = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    satisfaccion = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    actualizado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo