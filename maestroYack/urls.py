"""
URL configuration for maestroYack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicaciones.gestionContactos import views  # Importa las vistas desde la aplicación gestionContactos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agregar_contacto/', views.agregar_contacto, name='agregar_contacto'),
    path('lista_contactos/', views.lista_contactos, name='lista_contactos'),
    path('eliminar_contacto/<int:id_contacto>/', views.eliminar_contacto, name='eliminar_contacto'),
    path('editar_contacto/<int:id_contacto>/', views.editar_contacto, name='editar_contacto'),
    path('agregar_ciudad/', views.agregar_ciudad, name='agregar_ciudad'),  # Nueva URL para agregar ciudades
    path('editar_ciudad/<int:id_ciudad>/', views.editar_ciudad, name='editar_ciudad'),
    path('eliminar_ciudad/<int:id_ciudad>/', views.eliminar_ciudad, name='eliminar_ciudad'),
    path('agregar_empresa/', views.agregar_empresa, name='agregar_empresa'),  # Nueva URL para agregar empresas
    path('editar_empresa/<str:id_empresa>/', views.editar_empresa, name='editar_empresa'),
    path('eliminar_empresa/<str:id_empresa>/', views.eliminar_empresa, name='eliminar_empresa'),
    path('lista_empresas/', views.lista_empresas, name='lista_empresas'),
    path('lista_ciudades/', views.lista_ciudades, name='lista_ciudades'),
]
