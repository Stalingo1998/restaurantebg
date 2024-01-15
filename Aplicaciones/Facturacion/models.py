from django.db import models

# Create your models here.
from django.db import models

class Provincia(models.Model):
    id_bg = models.AutoField(primary_key=True)
    nombre_bg = models.CharField(max_length=100)
    poblacion_bg = models.IntegerField()
    capital_bg = models.CharField(max_length=50)
    fotografia=models.FileField(upload_to='provincia', null=True,blank=True)

    def __str__(self):
        fila="{0}: {1} {2} {3}"
        return fila.format(self.id_bg, self.nombre_bg, self.poblacion_bg, self.capital_bg)


class Tipo(models.Model):
    id_bg = models.AutoField(primary_key=True)
    nombre_bg = models.CharField(max_length=150)
    descripcion_bg = models.TextField()
    fotografia=models.FileField(upload_to='tipo', null=True,blank=True)

    def __str__(self):
        fila="{0}: {1} {2} "
        return fila.format(self.id_bg, self.nombre_bg, self.descripcion_bg)



class Cliente(models.Model):
    id_bg = models.AutoField(primary_key=True)
    cedula_bg = models.CharField(max_length=10)
    apellido_bg = models.CharField(max_length=150)
    nombre_bg = models.CharField(max_length=150)
    direccion_bg = models.TextField()
    fecha_nacimiento_bg = models.DateField()
    correo_bg = models.EmailField()
    provincia_bg = models.ForeignKey(Provincia, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        fila="{0}: {1} {2} {3} {4} {5} {6}"
        return fila.format(self.id_bg, self.cedula_bg, self.apellido_bg, self.nombre_bg, self.direccion_bg, self.fecha_nacimiento_bg,self.correo_bg)



class Pedido(models.Model):
    id_bg = models.AutoField(primary_key=True)
    fecha_bg = models.DateField()
    estado_bg = models.CharField(max_length=50)
    observaciones_bg = models.TextField()
    cliente_bg = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.PROTECT)


    def __str__(self):
        fila="{0}: {1} {2} "
        return fila.format(self.id_bg, self.fecha_bg, self.estado_bg)





class Platillo(models.Model):
    id_bg = models.AutoField(primary_key=True)
    nombre_bg = models.CharField(max_length=100)
    precio_bg = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad_bg = models.CharField(max_length=50)
    fotografia=models.FileField(upload_to='platillo', null=True,blank=True)
    tipo_bg = models.ForeignKey(Tipo, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        fila="{0}: {1} {2} {3}"
        return fila.format(self.id_bg, self.nombre_bg, self.precio_bg, self.disponibilidad_bg)




class DetallePlatillo(models.Model):
    id_bg = models.AutoField(primary_key=True)
    descripcion_bg = models.TextField()
    calorias_bg = models.IntegerField()
    fecha_bg = models.DateField()
    pedido_bg = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.PROTECT)
    platillo_bg = models.ForeignKey(Platillo, null=True, blank=True, on_delete=models.PROTECT)


    def __str__(self):
        fila="{0}: {1} {2} {3}"
        return fila.format(self.id_bg, self.descripcion_bg, self.calorias_bg, self.fecha_bg)



class Ingrediente(models.Model):
    id_bg = models.AutoField(primary_key=True)
    nombre_bg = models.CharField(max_length=100)
    cantidad_disponible_bg = models.CharField(max_length=100)
    unidad_medida_bg = models.CharField(max_length=20)
    fecha_caducidad_bg = models.DateField()
    fotografia=models.FileField(upload_to='ingrediente', null=True,blank=True)


    def __str__(self):
        fila="{0}: {1} {2} {3} {4}"
        return fila.format(self.id_bg, self.nombre_bg, self.cantidad_disponible_bg, self.unidad_medida_bg, self.fecha_caducidad_bg, self.fotografia)



class Receta(models.Model):
    id_bg = models.AutoField(primary_key=True)
    cantidad_bg = models.CharField(max_length=100)
    procedimiento_bg = models.CharField(max_length=500)
    platillo_bg = models.ForeignKey(Platillo, on_delete=models.PROTECT)
    ingrediente_bg = models.ForeignKey(Ingrediente, null=True, blank=True, on_delete=models.PROTECT)


    def __str__(self):
        fila="{0}: {1} {2} "
        return fila.format(self.id_bg, self.cantidad_bg, self.procedimiento_bg)
