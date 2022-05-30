from django.db import models

# Create your models here.


#MODELO PARA EL USUARIO

class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=50,verbose_name="Nombre de usuario")
    correo = models.CharField(max_length=50,verbose_name="Correo")
    fechaNac = models.CharField(max_length=50,verbose_name="Fecha de nacimiento")
    contra = models.CharField(max_length=50,verbose_name="Contraseña")

    def __str__(self):
        return self.nombreUsuario


#MODELO PARA PRODUCTO

class Producto(models.Model):
    precio = models.IntegerField(verbose_name="Precio")
    nombreSkin = models.CharField(max_length=50,verbose_name="Nombre de la skin")
    categoria = models.CharField(max_length=30,verbose_name="Categoria")
    imagenSkin = models.ImageField(upload_to="skins", null= True)
    descripcion = models.CharField(max_length=50,verbose_name="Descripcion")


    def __str__(self):
        return self.nombreSkin

