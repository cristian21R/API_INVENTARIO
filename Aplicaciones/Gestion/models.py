from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    marca = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre


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

    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
