#listings/views.py
from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Listing

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', context={'bands' : bands})

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request,
            'listings/band_detail.html',
            {'band' : band}
    )


def about(request):
    return render(request, 'about.html')

def list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing.html', context={'listings' : listings})    

def contact(request):
    return render(request, 'contact.html')      