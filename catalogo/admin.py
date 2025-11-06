from django.contrib import admin
from .models import Categoria, Etiqueta, Producto, DetalleProducto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ( 'nombre', )
	search_fields = ('nombre',)


@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
	list_display = ( 'nombre', )
	search_fields = ('nombre',)


class DetalleProductoInline(admin.StackedInline):
	model = DetalleProducto
	extra = 0
	can_delete = False


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'categoria', 'precio')
	list_filter = ('categoria', 'etiquetas')
	search_fields = ('nombre', 'descripcion')
	inlines = [DetalleProductoInline]

# Register your models here.
