#listings/views.py
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail

from listings.models import Band, Listing
from listings.forms import ContactForm, BandForm, ListingForm

#
# 1) Band
#
def band_list(request):
    bands = Band.objects.all()
    return render(request, 
                'listings/band_list.html', 
                context={'bands' : bands}
                )

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request,
                'listings/band_detail.html',
                context={'band' : band}
                )

def band_create(request):
    
    if request.method == "POST":

        form = BandForm(request.POST)

        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
        

    else:
        form = BandForm()

    return render(request, 
                'listings/band_create.html',
                {'form' : form}
                )      

#
# 2) Listing
#
def list(request):
    listings = Listing.objects.all()
    return render(request, 
                'listings/listing.html', 
                context={'listings' : listings}
                )   

def list_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, 
                'listings/listing_detail.html', 
                context={'listing' : listing}
                )       


def list_create(request):
    
    if request.method == "POST":

        form = ListingForm(request.POST)

        if form.is_valid():
            list = form.save()
            return redirect('post-detail', list.id)
        

    else:
        form = ListingForm()

    return render(request, 
                'listings/listing_create.html',
                {'form' : form}
                )      

#
# 3) Contact
#
def contact(request):

    # Formulaire
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via Contact Form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@jestocke.com'],
            )
        
            return redirect('email-sent')
    
    # method = "GET", vide. On lui donne rien.
    else:
        form = ContactForm()

    return render(request, 
                'listings/contact.html',
                context={'form' : form}
                )      

def email_sent(request):

    return render(request, 'email_sent.html')

#
# 4) About
#
def about(request):
    return render(request, 'about.html')