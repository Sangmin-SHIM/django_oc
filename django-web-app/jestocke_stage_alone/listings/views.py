#listings/views.py
from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Listing

def tuto(request):
    bands = Band.objects.all()
    return render(request, 'listings/tuto.html', context={'bands' : bands})

def about(request):
    return render(request, 'about.html')

def list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing.html', context={'listings' : listings})    

def contact(request):
    return render(request, 'contact.html')      