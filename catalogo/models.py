from django.db import models


class Categoria(models.Model):
	nombre = models.CharField(max_length=100, unique=True)
	descripcion = models.TextField(blank=True)

	class Meta:
		verbose_name = 'Categoría'
		verbose_name_plural = 'Categorías'
		ordering = ['nombre']

	def __str__(self) -> str:
		return self.nombre


class Etiqueta(models.Model):
	nombre = models.CharField(max_length=50, unique=True)

	class Meta:
		verbose_name = 'Etiqueta'
		verbose_name_plural = 'Etiquetas'
		ordering = ['nombre']

	def __str__(self) -> str:
		return self.nombre


class Producto(models.Model):
	nombre = models.CharField(max_length=150)
	descripcion = models.TextField(blank=True)
	precio = models.DecimalField(max_digits=10, decimal_places=2)
	categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='productos')
	etiquetas = models.ManyToManyField(Etiqueta, blank=True, related_name='productos')

	class Meta:
		ordering = ['nombre']

	def __str__(self) -> str:
		return f"{self.nombre} ({self.categoria})"


class DetalleProducto(models.Model):
	producto = models.OneToOneField(Producto, on_delete=models.CASCADE, related_name='detalle')
	dimension = models.CharField(max_length=100, blank=True, help_text='Ej: 10x20x30 cm')
	peso = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text='Peso en kg')

	class Meta:
		verbose_name = 'Detalle de Producto'
		verbose_name_plural = 'Detalles de Productos'

	def __str__(self) -> str:
		return f"Detalle de {self.producto.nombre}"
