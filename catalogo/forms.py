from django import forms
from .models import Producto, Categoria, Etiqueta, DetalleProducto


class ProductoForm(forms.ModelForm):
    # Campos para el modelo uno-a-uno DetalleProducto
    dimension = forms.CharField(required=False, label='Dimensión', help_text='Ej: 10x20x30 cm')
    peso = forms.DecimalField(required=False, label='Peso (kg)', max_digits=10, decimal_places=2)

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'etiquetas', 'dimension', 'peso']
        widgets = {
            'etiquetas': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Precargar los campos de detalle si existen
        if self.instance and getattr(self.instance, 'detalle', None):
            self.fields['dimension'].initial = self.instance.detalle.dimension
            self.fields['peso'].initial = self.instance.detalle.peso

    def save(self, commit=True):
        producto = super().save(commit)
        dimension = self.cleaned_data.get('dimension')
        peso = self.cleaned_data.get('peso')
        detalle, _created = DetalleProducto.objects.get_or_create(producto=producto)
        detalle.dimension = dimension or ''
        detalle.peso = peso
        if commit:
            detalle.save()
        return producto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']


class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ['nombre']
