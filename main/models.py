# app/models.py
from django.db import models
import os
from uuid import uuid4


def user_foto_path(instance, filename):
    ext = filename.split('.')[-1]
    nombre_archivo = f"{instance.numero_celular}_{uuid4().hex}.{ext}"
    return os.path.join('fotos', nombre_archivo)

class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=200)
    numero_celular = models.CharField(max_length=15, unique=True)
    foto = models.ImageField(upload_to=user_foto_path, blank=True, null=True)

    def __str__(self):
        return self.nombre_completo
