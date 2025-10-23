from django.db import models


class Antiguedad(models.Model):
	"""Modelo mínimo para representar una antigüedad/objeto.

	Ajustado para coincidir con los formularios y plantillas del proyecto.
	Campos principales:
	- nombre_pieza: texto descriptivo que se muestra en las plantillas
	- precio: valor numérico con decimales
	"""
	nombre_pieza = models.CharField(max_length=200)
	precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	descripcion = models.TextField(blank=True)
	fecha = models.DateField(null=True, blank=True)
	creado = models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:
		return self.nombre_pieza

