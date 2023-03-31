from django.shortcuts import render
from django.http import HttpResponse
from json import loads,dumps
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from . serializers import usuariosSerializer, partidasSerializer
from . models import usuarios, partidas
import sqlite3

# Create your views here.

def index(request):
    return render(request, 'index.html')

class usuariosViewSet(viewsets.ModelViewSet):
    queryset = usuarios.objects.all()
    serializer_class = usuariosSerializer

class partidasViewSet(viewsets.ModelViewSet):
    queryset = partidas.objects.all()
    serializer_class = partidasSerializer

