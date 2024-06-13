from django.db import models

# Create your models here.
class Huesped(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    edad=models.CharField(max_length=3)
    nacionalidad=models.CharField(max_length=20)
    
    def __str__(self):
        return f'Se ha registrado El/la huesped {self.nombre} {self.apellido} de {edad} años de nacionalidad {nacionalidad}'
    
