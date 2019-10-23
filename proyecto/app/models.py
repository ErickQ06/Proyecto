from django.db import models


# Create your models here.




class tipoMaterial(models.Model):
	codigo=models.CharField(max_length=4)
	nombre=models.CharField(max_length=50)
	precio=models.DecimalField(max_digits=5, decimal_places=2)

	class Meta:
		"""docstring for Meta"""
		verbose_name='tipoMaterial'
		verbose_name_plural='tipoMateriales'
	def __str__(self):
		return '%s' %(self.nombre)

class empresa(models.Model):
	codigoMat=models.ManyToManyField(tipoMaterial)
	nombreEmpresa=models.CharField(max_length=200)
	telefono=models.CharField(max_length=9)
	direccion=models.CharField(max_length=200)
	email=models.EmailField(null=True, blank=True)
	web=models.CharField(max_length=100)
	contacto=models.CharField(max_length=100)
	servicio=models.CharField(max_length=200)
	materiales=models.CharField(max_length=200)

	class Meta:
		verbose_name='Empresa'
		verbose_name_plural='Empresas'
		def __str__(self):
			return '%s' %(self.nombreEmpresa)