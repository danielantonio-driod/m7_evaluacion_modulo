from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.db import connection
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Producto, Categoria, Etiqueta, DetalleProducto
from .forms import ProductoForm, CategoriaForm, EtiquetaForm


class ProductoListView(ListView):
	model = Producto
	context_object_name = 'productos'
	template_name = 'productos/lista.html'
	paginate_by = 10

	def get_queryset(self):
		qs = (
			Producto.objects.select_related('categoria')
			.prefetch_related('etiquetas')
			.all()
		)
		q = self.request.GET.get('q')
		categoria_id = self.request.GET.get('categoria')
		min_price = self.request.GET.get('min_price')
		max_price = self.request.GET.get('max_price')

		if q:
			qs = qs.filter(Q(nombre__icontains=q) | Q(descripcion__icontains=q))
		if categoria_id:
			qs = qs.filter(categoria_id=categoria_id)
		if min_price:
			qs = qs.filter(precio__gte=min_price)
		if max_price:
			qs = qs.filter(precio__lte=max_price)

		# Example of exclude() usage: exclude products with empty description
		if self.request.GET.get('sin_descripcion') == '1':
			qs = qs.exclude(descripcion='')

		return qs

	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs)
		ctx['categorias'] = Categoria.objects.all()
		return ctx


class ProductoDetailView(DetailView):
	model = Producto
	context_object_name = 'producto'
	template_name = 'productos/detalle.html'


class ProductoCreateView(LoginRequiredMixin, CreateView):
	model = Producto
	form_class = ProductoForm
	template_name = 'productos/crear.html'
	success_url = reverse_lazy('productos_lista')


class ProductoUpdateView(LoginRequiredMixin, UpdateView):
	model = Producto
	form_class = ProductoForm
	template_name = 'productos/editar.html'
	success_url = reverse_lazy('productos_lista')


class ProductoDeleteView(LoginRequiredMixin, DeleteView):
	model = Producto
	template_name = 'productos/eliminar.html'
	success_url = reverse_lazy('productos_lista')


class CategoriaListView(ListView):
	model = Categoria
	context_object_name = 'categorias'
	template_name = 'categorias/lista.html'


class CategoriaCreateView(LoginRequiredMixin, CreateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'categorias/formulario.html'
	success_url = reverse_lazy('categorias_lista')


class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'categorias/formulario.html'
	success_url = reverse_lazy('categorias_lista')


class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
	model = Categoria
	template_name = 'categorias/eliminar.html'
	success_url = reverse_lazy('categorias_lista')


class EtiquetaListView(ListView):
	model = Etiqueta
	context_object_name = 'etiquetas'
	template_name = 'etiquetas/lista.html'


class EtiquetaCreateView(LoginRequiredMixin, CreateView):
	model = Etiqueta
	form_class = EtiquetaForm
	template_name = 'etiquetas/formulario.html'
	success_url = reverse_lazy('etiquetas_lista')


class EtiquetaUpdateView(LoginRequiredMixin, UpdateView):
	model = Etiqueta
	form_class = EtiquetaForm
	template_name = 'etiquetas/formulario.html'
	success_url = reverse_lazy('etiquetas_lista')


class EtiquetaDeleteView(LoginRequiredMixin, DeleteView):
	model = Etiqueta
	template_name = 'etiquetas/eliminar.html'
	success_url = reverse_lazy('etiquetas_lista')


def categorias_conteo(request):
	categorias = Categoria.objects.annotate(productos_count=Count('productos')).order_by('-productos_count')
	return render(request, 'categorias/reporte_conteo.html', {'categorias': categorias})


def productos_raw_mayor_precio(request):
	try:
		minimo = float(request.GET.get('min', '0'))
	except ValueError:
		minimo = 0
	# raw SQL example with parameters to avoid SQL injection
	productos = list(Producto.objects.raw(
		'SELECT p.id, p.nombre, p.descripcion, p.precio, p.categoria_id FROM catalogo_producto p WHERE p.precio > %s',
		[minimo]
	))
	return render(request, 'productos/raw.html', {'productos': productos, 'minimo': minimo})

# Create your views here.
