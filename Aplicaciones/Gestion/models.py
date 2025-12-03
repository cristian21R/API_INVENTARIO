from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200, blank=True, null=True)


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,   
        related_name='productos'
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2)