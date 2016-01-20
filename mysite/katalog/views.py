from django.shortcuts import render
from django.http import HttpResponse
from .models import Tovar
from django.shortcuts import render, get_object_or_404

def moloko_list(request):
    moloko=Tovar.objects.filter(category__name='moloko')
    return render(request, 'katalog/moloko_list.html', {'moloko':moloko})

def myaso_list(request):
    myaso=Tovar.objects.filter(category__name='myaso')
    return render(request, 'katalog/myaso_list.html', {'myaso':myaso})

def pivo_list(request):
    pivo=Tovar.objects.filter(category__name='pivo')
    return render(request, 'katalog/pivo_list.html', {'pivo':pivo})

def gigiena_list(request):
    gigiena=Tovar.objects.filter(category__name='gigiena')
    return render(request, 'katalog/gigiena_list.html', {'gigiena':moloko})

def tovar_detail(request, pk):
    tovar = get_object_or_404(Tovar, pk=pk)
    return render(request, 'katalog/tovar_detail.html', {'tovar': tovar})
