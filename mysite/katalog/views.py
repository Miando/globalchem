from django.shortcuts import render
from django.http import HttpResponse

def tovar_list(request):
    return render(request, 'katalog/tovar_list.html', {})
