from django.shortcuts import render
from django.http import HttpResponse
from .models import Tovar

def tovar_list(request):
    tovars=Tovar.objects.filter(category__name='Moloko')
    return render(request, 'katalog/tovar_list.html', {'tovars':tovars})
