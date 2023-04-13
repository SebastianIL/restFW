# models.py
from django.db import models
class usuarios(models.Model):
    password = models.CharField(max_length=60)

class partidas(models.Model):
    fecha = models.CharField(max_length=60)
    id_usuarios = models.ForeignKey(usuarios, related_name="id_usuario", on_delete=models.CASCADE)
    #id_usuarios = models.ForeignKey(usuarios, related_name="id_usuarios", on_delete=models.CASCADE)
    #models.ForeignKey(User, on_delete=models.CASCADE)
    minutos_jugados= models.IntegerField()
    puntaje=models.IntegerField()
    nivel=models.CharField(max_length=50, blank=True)
    intentos=models.IntegerField(default=0)