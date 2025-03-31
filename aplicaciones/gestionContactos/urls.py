from django.urls import path
from . import views

urlpatterns = [
    path('agregar_contacto/', views.agregar_contacto, name='agregar_contacto'),
]