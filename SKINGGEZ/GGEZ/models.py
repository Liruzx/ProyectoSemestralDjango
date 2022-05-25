from django.db import models

# Create your models here.


#MODELO PARA EL USUARIO

class Usuario(models.Model):
    idCliente = models.IntegerField(primary_key=True, verbose_name="Id de usuario")
    nombreUsuario = models.CharField(max_length=50,verbose_name="Nombre de usuario",blank=False,null=False)
    correo = models.CharField(max_length=50,verbose_name="Correo",blank=False,null=False)
    fechaNac = models.CharField(max_length=50,verbose_name="Fecha de nacimiento",blank=False,null=False)
    contra = models.CharField(max_length=50,verbose_name="Contraseña",blank=False,null=False)

    def __str__(self):
        return self.nombreUsuario


#MODELO PARA PRODUCTO

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="Id de usuario")
    precio = models.IntegerField(verbose_name="Precio",blank=False,null=False)
    nombreSkin = models.CharField(max_length=50,verbose_name="Nombre de la skin",blank=False,null=False)
    categoria = models.CharField(max_length=30,verbose_name="Categoria",blank=False,null=False)
    imagenSkin = models.ImageField(upload_to="skins", null= True)
    descripcion = models.CharField(max_length=50,verbose_name="Descripcion")


    def __str__(self):
        return self.nombreSkin

