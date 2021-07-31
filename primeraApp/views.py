from django.shortcuts import render, HttpResponse
import datetime
import time

def index(request):
    fecha = {
        'fecha' : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'fecha2' : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
    }
    return render(request, 'index.html' , fecha)