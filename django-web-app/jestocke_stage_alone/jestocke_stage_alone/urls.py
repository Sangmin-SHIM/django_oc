from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    
    # bands
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:band_id>/', views.band_detail, name = 'band-detail'),
    path('bands/add/', views.band_create, name='band-create'),
    
    
    # listings
    path('listing/', views.list, name='post-list'),
    path('listing/<int:listing_id>/', views.list_detail, name='post-detail'),
    path('listing/add/', views.list_create, name='post-create'),

    
    # Contact
    path('contact/', views.contact, name = 'contact'),
    path('email-sent/', views.email_sent, name = 'email-sent'),

    # info
    path('about/', views.about, name='about'),

]