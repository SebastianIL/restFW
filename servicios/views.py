from django.shortcuts import render
from django.http import HttpResponse
from json import loads,dumps
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from . serializers import usuariosSerializer, partidasSerializer
from . models import usuarios, partidas
import sqlite3
import random
import string
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')

class usuariosViewSet(viewsets.ModelViewSet):
    queryset = usuarios.objects.all()
    serializer_class = usuariosSerializer

class partidasViewSet(viewsets.ModelViewSet):
    queryset = partidas.objects.all()
    serializer_class = partidasSerializer

def grafica(request):
    '''
    print("Si llega aqui")
    t_var = 'jugador'
    h_var = 'Intentos'
    v_var = 'Puntaje'
    f_var = 'Nivel'
    z_var = 'Tiempo'
    rest = partidas.objects.all()
    data = ([t_var,h_var,v_var,f_var,z_var])
    
    for i in rest:
        idus = i.id_usuarios
        intento = i.intentos
        puntaje = i.puntaje
        nivel = i.nivel
        tiempo = i.minutos_jugados
        data.append([idus,intento,puntaje,nivel,tiempo])
    
    t_var_JSON = dumps(t_var)
    h_var_JSON = dumps(h_var)
    v_var_JSON = dumps(v_var)
    z_var_JSON = dumps(z_var)
    modified_data = dumps(data)
    print("Si llega al return")
    elJSON = {'losDatos':modified_data,'h_title':h_var_JSON,'v_title':v_var_JSON,'z_title':z_var_JSON}
    return render (request,"charts.html",elJSON)
    '''
    data = []
    data.append(['jugador', 'Intentos','Puntaje','Nivel','Tiempo'])
    #resultados = partidas.objects.all() #select * from reto;
    titulo = 'Fraliens'
    titulo_formato = dumps(titulo)
    subtitulo= 'X=Intentos, Y=Puntajes, Bubble size=Tiempo, Bubble color=Nivel'
    subtitulo_formato = dumps(subtitulo)
    url = "http://127.0.0.1:8000/apipartidas"
    header={
        "Content-Type":"application/json"
    }
    
    result = requests.get(url, headers=header)
    resultjson= result.json()
    for i in range(len(resultjson)):
        idtemp=resultjson[i]['id_usuarios']
        idclean=idtemp[-2]
        data.append([idclean, resultjson[i]['intentos'],resultjson[i]['puntaje'],resultjson[i]['nivel'],resultjson[i]['minutos_jugados']])

    data_formato = dumps(data) #formatear los datos en string para JSON
    myJSON = {'values':data_formato,'titulo':titulo_formato,'subtitulo':subtitulo_formato}
    return render(request,'charts.html',myJSON)
