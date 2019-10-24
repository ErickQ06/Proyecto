from django.shortcuts import render
from .models import*
from django.urls import *


# Create your views here.



def verMaterial(request):
	material = tipoMaterial.objects.all()
	return render(request, 'verMaterial.html', {'material':material, })

def verEmpresa(request):
	empresas = empresa.objects.all()
	
	return render(request, 'verEmpresa.html', {'empresas':empresas, })

def valorRecuperacion(request):
	return render(request, 'valorRecuperacion.html')

def perdidaMonetaria(request):
	return render(request, 'perdidaMonetaria.html')

def index(request):
	return render(request, 'index.html')

def listaEmpresa(request, codigo):
	listaEmpresas = empresa.objects.filter(codigoMat=codigo)
	return render(request, 'listaEmpresa.html', {'listaEmpresas': listaEmpresas, })

def informacionEmpresa(request, emp):
	lisEmp = empresa.objects.filter(id=emp)
	return render(request, 'informacionEmpresa.html', {'lisEmp': lisEmp, })


	