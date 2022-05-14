#listings/views.py

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django ! Hello JeStocke !</h1>')

def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous adorons JeStocke !</p>')

def list(request):
    return HttpResponse('<h1>Listing</h1> <p>Nous adorons JeStocke !</p>')    

def contact(request):
    return HttpResponse('<h1>Contact Us</h1> <p>Nous adorons JeStocke !</p>')      