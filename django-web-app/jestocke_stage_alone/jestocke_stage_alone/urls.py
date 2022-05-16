from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tuto/', views.tuto),
    path('about/', views.about),
    path('listing/', views.list),
    path('contact/', views.contact),
]