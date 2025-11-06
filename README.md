# Tienda (Django + PostgreSQL)

Aplicación de ejemplo para gestionar Productos y sus relaciones con Categorías, Etiquetas y Detalles (uno a uno). Incluye CRUD completo, búsquedas y filtros con el ORM, ejemplo de anotaciones y una vista con SQL RAW.

## Requisitos
- Python 3.10+
- PostgreSQL (opcional si usas SQLite para pruebas locales)

## Instalación
1. Crear y activar entorno virtual (ya creado en este repo como `.venv`).
2. Instalar dependencias (si hacen falta):

```powershell
# Si no están instaladas
pip install django psycopg2-binary
```

3. La configuración de base de datos está fija en `tienda/settings.py` para PostgreSQL local:

```
ENGINE=django.db.backends.postgresql
NAME=tienda_db
USER=root
PASSWORD=root
HOST=localhost
PORT=5432
```

4. Migraciones:

```powershell
python manage.py makemigrations
python manage.py migrate
```

5. Crear superusuario para el admin:

```powershell
python manage.py createsuperuser
```

6. Ejecutar:

```powershell
python manage.py runserver
```

## Rutas principales
- `/` Inicio
- `/productos/` Lista de productos con filtros (`q`, `categoria`, `min_price`, `max_price`, `sin_descripcion=1`)
- `/productos/crear/` Crear producto (requiere login)
- `/productos/<id>/` Detalle
- `/productos/<id>/editar/` Editar (requiere login)
- `/productos/<id>/eliminar/` Eliminar (requiere login)
- `/categorias/` Lista
- `/categorias/crear/`, `/categorias/<id>/editar/`, `/categorias/<id>/eliminar/`
- `/etiquetas/` Lista
- `/etiquetas/crear/`, `/etiquetas/<id>/editar/`, `/etiquetas/<id>/eliminar/`
- `/reportes/categorias/` Anotación: conteo de productos por categoría
- `/productos/raw-alto-precio/?min=100` Ejemplo de SQL raw
- `/admin/` Admin de Django
- `/accounts/login` y `/accounts/logout/` Autenticación

## Modelos y relaciones
- `Producto` — muchos a uno con `Categoria`
- `Producto` — muchos a muchos con `Etiqueta`
- `Producto` — uno a uno con `DetalleProducto`

## Seguridad
- CSRF habilitado en formularios (`{% csrf_token %}`)
- Vistas de creación/edición/eliminación protegidas con login
- Middleware de seguridad de Django activo; para producción ajusta `DEBUG=False`, `ALLOWED_HOSTS` y activa cookies seguras/HSTS en `settings.py`.

## Notas
- El admin permite gestionar todo y ver/editar `DetalleProducto` en línea dentro de `Producto`.
 - Si prefieres variables de entorno o `.env`, puedes adaptar `settings.py`, pero este repo está listo con configuración fija para desarrollo local.
