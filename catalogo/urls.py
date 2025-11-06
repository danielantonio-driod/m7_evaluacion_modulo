from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.ProductoListView.as_view(), name='productos_lista'),
    path('productos/crear/', views.ProductoCreateView.as_view(), name='productos_crear'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='productos_detalle'),
    path('productos/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='productos_editar'),
    path('productos/<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='productos_eliminar'),

    path('categorias/', views.CategoriaListView.as_view(), name='categorias_lista'),
    path('categorias/crear/', views.CategoriaCreateView.as_view(), name='categorias_crear'),
    path('categorias/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='categorias_editar'),
    path('categorias/<int:pk>/eliminar/', views.CategoriaDeleteView.as_view(), name='categorias_eliminar'),

    path('etiquetas/', views.EtiquetaListView.as_view(), name='etiquetas_lista'),
    path('etiquetas/crear/', views.EtiquetaCreateView.as_view(), name='etiquetas_crear'),
    path('etiquetas/<int:pk>/editar/', views.EtiquetaUpdateView.as_view(), name='etiquetas_editar'),
    path('etiquetas/<int:pk>/eliminar/', views.EtiquetaDeleteView.as_view(), name='etiquetas_eliminar'),

    path('reportes/categorias/', views.categorias_conteo, name='reporte_categorias'),
    path('productos/raw-alto-precio/', views.productos_raw_mayor_precio, name='productos_raw_mayor_precio'),
]
