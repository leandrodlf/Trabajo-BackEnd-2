from django.db import models

class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=5)
    cli_nombre = models.CharField(max_length=40)
    cli_contacto = models.CharField(max_length=30)
    cli_titulo_contacto = models.CharField(max_length=30)
    cli_direccion = models.CharField(max_length=60)
    cli_ciudad = models.CharField(max_length=15)
    cli_region = models.CharField(max_length=15)
    cli_codigo_postal = models.CharField(max_length=10)
    cli_pais = models.CharField(max_length=15)
    cli_telefono = models.CharField(max_length=24)
    cli_mail = models.CharField(max_length=24)

    def __str__(self):
        return self.cli_nombre

class Empleado(models.Model):
    id_empleado = models.BigAutoField(primary_key=True)
    emp_nombre = models.CharField(max_length=20)
    emp_apellido = models.CharField(max_length=10)
    emp_titulo = models.CharField(max_length=30)
    emp_mail = models.CharField(max_length=25)
    emp_fecha_nac = models.DateField()
    emp_fecha_contrato = models.DateField()
    emp_direccion = models.CharField(max_length=60)
    emp_celular = models.CharField(max_length=24)
    emp_foto = models.BinaryField()
    emp_notas = models.TextField()

    def __str__(self):
        return f"{self.emp_nombre} {self.emp_apellido}"

class Categoria(models.Model):
    id_categoria = models.BigAutoField(primary_key=True)
    cat_nombre = models.CharField(max_length=15)
    cat_desc = models.TextField() 
    cat_foto = models.BinaryField()

    def __str__(self):
        return self.cat_nombre

class Producto(models.Model):
    id_producto = models.BigAutoField(primary_key=True)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    pro_nombre = models.CharField(max_length=40)
    pro_descripcion = models.CharField(max_length=30)
    pro_precio = models.DecimalField(max_digits=19, decimal_places=4)
    pro_stock = models.IntegerField()

    def __str__(self):
        return self.pro_nombre

class Orden(models.Model):
    id_orden = models.BigAutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    ord_fecha = models.DateField()

    def __str__(self):
        return f"Orden {self.id_orden}"

class DetalleOrden(models.Model):
    id_detord = models.BigAutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    deo_precio = models.FloatField()
    deo_cantidad = models.IntegerField()
    id_orden = models.ForeignKey(Orden, on_delete=models.CASCADE)

    def __str__(self):
        return f"Detalle {self.id_detord} - Producto {self.id_producto.pro_nombre}"

class Proveedor(models.Model):
    id_proveedor = models.BigAutoField(primary_key=True)
    prv_empresa = models.CharField(max_length=40)
    prv_giro = models.CharField(max_length=20)
    prv_contacto = models.CharField(max_length=30)
    prv_direccion = models.CharField(max_length=60)
    prv_pco_postal = models.CharField(max_length=10)
    prv_telefono = models.CharField(max_length=24)

    def __str__(self):
        return self.prv_empresa
