from django.db import models

# Create your models here.


#MODELO PARA EL USUARIO

class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=50 , unique=True ,verbose_name="Nombre de usuario")
    correo = models.CharField(max_length=50,unique=True,verbose_name="Correo")
    fechaNac = models.CharField(max_length=50,verbose_name="Fecha de nacimiento")
    contra = models.CharField(max_length=50,verbose_name="Contraseña")

    def __str__(self):
        return self.nombreUsuario


#MODELO PARA PRODUCTO LOL

class Producto(models.Model):
    precio = models.IntegerField(verbose_name="Precio")
    nombreSkin = models.CharField(max_length=50,verbose_name="Nombre de la skin")
    nombreUsuario = models.CharField(max_length=50,verbose_name="Nombre de usuario ")
    imagenSkin = models.ImageField(upload_to="skins", null= True)
    


    def __str__(self):
        return self.nombreSkin

#MODELO PRODUCTO VALO
class Producto2(models.Model):
    precio2 = models.IntegerField(verbose_name="Precio")
    nombreSkin2 = models.CharField(max_length=50,verbose_name="Nombre de la skin")
    nombreUsuario2 = models.CharField(max_length=50,verbose_name="Nombre de usuario ")
    imagenSkin2 = models.ImageField(upload_to="skins", null= True)
    


    def __str__(self):
        return self.nombreSkin2

#MODELO PRODUCTO CSGO

class Producto3(models.Model):
    precio3 = models.IntegerField(verbose_name="Precio")
    nombreSkin3 = models.CharField(max_length=50,verbose_name="Nombre de la skin")
    nombreUsuario3 = models.CharField(max_length=50,verbose_name="Nombre de usuario ")
    imagenSkin3 = models.ImageField(upload_to="skins", null= True)
    


    def __str__(self):
        return self.nombreSkin3



