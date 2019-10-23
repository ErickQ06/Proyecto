from django.contrib import admin
from .models import *

# Register your models here.

class EmpresaAdmin(admin.ModelAdmin):
	list_display = ('nombreEmpresa', 'telefono', 'direccion', 'email', 'web', 'contacto', 'servicio','materiales')
admin.site.register(empresa, EmpresaAdmin)

class TipoMaterialAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'nombre','precio')
admin.site.register(tipoMaterial, TipoMaterialAdmin)
