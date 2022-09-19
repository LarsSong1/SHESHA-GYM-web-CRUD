from django.db import models

# Create your models here.

class comentario(models.Model):
    texto = models.CharField(max_length=200)


class register_data(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    contraseña_usuario = models.CharField(max_length=50)
    verificacion_contraseña = models.CharField(max_length=50)
    

