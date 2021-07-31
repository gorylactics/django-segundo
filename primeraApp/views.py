from django.shortcuts import render, HttpResponse
import datetime

def index(request):
    fecha = {
        'fecha' : datetime.datetime.now(),
    }
    return render(request, 'index.html' , fecha)