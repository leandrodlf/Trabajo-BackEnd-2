from django.contrib import admin
from django.utils.html import format_html
from .models import Cliente, Empleado, Categoria, Producto, Orden, DetalleOrden, Proveedor

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id_cliente',
        'cli_nombre',
        'cli_contacto',
        'cli_titulo_contacto',
        'cli_direccion',
        'cli_ciudad',
        'cli_region',
        'cli_codigo_postal',
        'cli_pais',
        'cli_telefono',
        'cli_mail',
    )
    search_fields = ('cli_nombre', 'cli_contacto', 'cli_telefono', 'cli_mail', 'cli_ciudad', 'cli_pais')
    list_filter = ('cli_ciudad', 'cli_region', 'cli_pais')
    ordering = ('cli_nombre',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id_empleado',
        'emp_nombre',
        'emp_apellido',
        'emp_titulo',
        'emp_mail',
        'emp_fecha_nac',
        'emp_fecha_contrato',
        'emp_direccion',
        'emp_celular',
        'foto_preview',
    )
    search_fields = ('emp_nombre', 'emp_apellido', 'emp_mail', 'emp_celular')
    list_filter = ('emp_fecha_nac', 'emp_fecha_contrato')
    ordering = ('emp_apellido',)

    def foto_preview(self, obj):
        if obj.emp_foto:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;"/>', obj.emp_foto.url)
        return "-"
    foto_preview.short_description = "Foto"

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'cat_nombre', 'cat_desc', 'foto_preview')
    search_fields = ('cat_nombre',)
    ordering = ('cat_nombre',)

    def foto_preview(self, obj):
        if obj.cat_foto:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;"/>', obj.cat_foto.url)
        return "-"
    foto_preview.short_description = "Foto"

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'id_producto',
        'pro_nombre',
        'id_categoria',
        'pro_descripcion',
        'pro_precio',
        'pro_stock',
    )
    search_fields = ('pro_nombre', 'pro_descripcion')
    list_filter = ('id_categoria',)
    ordering = ('pro_nombre',)

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id_orden', 'id_cliente', 'id_empleado', 'ord_fecha')
    search_fields = ('id_cliente__cli_nombre', 'id_empleado__emp_nombre')
    list_filter = ('ord_fecha',)
    ordering = ('ord_fecha',)

@admin.register(DetalleOrden)
class DetalleOrdenAdmin(admin.ModelAdmin):
    list_display = ('id_detord', 'id_orden', 'id_producto', 'deo_precio', 'deo_cantidad')
    search_fields = ('id_producto__pro_nombre',)
    ordering = ('id_detord',)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = (
        'id_proveedor',
        'prv_empresa',
        'prv_giro',
        'prv_contacto',
        'prv_direccion',
        'prv_pco_postal',
        'prv_telefono',
    )
    search_fields = ('prv_empresa', 'prv_contacto')
    ordering = ('prv_empresa',)
