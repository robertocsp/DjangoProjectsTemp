from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from administrativo.models import Marca

def usuario_marca(request):
    marca = Marca.objects.get(user=request.user)
    return HttpResponse('username: ' + request.user.username + ' // marca: ' + marca.nome)
