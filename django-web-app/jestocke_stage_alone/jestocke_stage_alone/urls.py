from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    
    # bands
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:band_id>/', views.band_detail),
    
    
    path('listing/', views.list),

    # info
    path('about/', views.about),
    path('contact/', views.contact),
]