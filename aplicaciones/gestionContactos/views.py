from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q  # Importar Q para búsquedas complejas
from .forms import ContactoPersonaForm, TelefonoForm, EmailForm, EmpresaForm, CiudadForm
from .models import contacto_persona, empresa, ciudad


def agregar_contacto(request):

    if request.method == 'POST':
        contacto_form = ContactoPersonaForm(request.POST)
        telefono_form = TelefonoForm(request.POST)
        email_form = EmailForm(request.POST)

        if contacto_form.is_valid() and telefono_form.is_valid() and email_form.is_valid():
            # Guardar el contacto
            contacto = contacto_form.save()

            # Guardar el teléfono asociado al contacto
            telefono = telefono_form.save(commit=False)
            telefono.persona = contacto
            telefono.save()

            # Guardar el email asociado al contacto
            email = email_form.save(commit=False)
            email.persona = contacto
            email.save()

            return redirect('lista_contactos')  # Redirigir a la lista de contactos
    else:
        contacto_form = ContactoPersonaForm()
        telefono_form = TelefonoForm()
        email_form = EmailForm()

    return render(request, 'gestionContactos/formulario_contacto.html', {
        'contacto_form': contacto_form,
        'telefono_form': telefono_form,
        'email_form': email_form,
    })


def lista_contactos(request):
    query = request.GET.get('q')  # Obtener el parámetro de búsqueda
    if query:
        # Filtrar contactos por nombre, apellido, ciudad, empresa o NIT de la empresa
        contactos = contacto_persona.objects.filter(
            Q(nombre_contacto__icontains=query) |
            Q(apellido_contacto__icontains=query) |
            Q(ciudad_contacto__nombre__icontains=query) |
            Q(empresa_contacto__nombre_empresa__icontains=query) |
            Q(empresa_contacto__nit_empresa__icontains=query)  # Filtro por NIT de la empresa
        ).prefetch_related('telefono_set', 'email_set')  # Optimizar consultas relacionadas
    else:
        # Si no hay búsqueda, mostrar todos los contactos
        contactos = contacto_persona.objects.all().prefetch_related('telefono_set', 'email_set')

    return render(request, 'gestionContactos/lista_contactos.html', {'contactos': contactos, 'query': query})


def agregar_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')  # Redirigir a la lista de contactos o donde prefieras
    else:
        form = EmpresaForm()
    return render(request, 'gestionContactos/formulario_empresa.html', {'form': form})


def agregar_ciudad(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')  # Redirigir a la lista de contactos o donde prefieras
    else:
        form = CiudadForm()
    return render(request, 'gestionContactos/formulario_ciudad.html', {'form': form})


def eliminar_contacto(request, id_contacto):
    contacto = get_object_or_404(contacto_persona, id_contacto=id_contacto)
    contacto.delete()
    return redirect('lista_contactos')  # Redirigir a la lista de contactos después de eliminar


def editar_contacto(request, id_contacto):
    contacto = get_object_or_404(contacto_persona, id_contacto=id_contacto)

    if request.method == 'POST':
        contacto_form = ContactoPersonaForm(request.POST, instance=contacto)
        if contacto_form.is_valid():
            contacto_form.save()
            return redirect('lista_contactos')  # Redirigir a la lista de contactos después de guardar
    else:
        contacto_form = ContactoPersonaForm(instance=contacto)

    return render(request, 'gestionContactos/formulario_editar_contacto.html', {
        'contacto_form': contacto_form,
        'contacto': contacto,
    })


def editar_ciudad(request, id_ciudad):
    ciudad = get_object_or_404(ciudad, id=id_ciudad)

    if request.method == 'POST':
        form = CiudadForm(request.POST, instance=ciudad)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')  # Redirigir a la lista de contactos o donde prefieras
    else:
        form = CiudadForm(instance=ciudad)

    return render(request, 'gestionContactos/formulario_editar_ciudad.html', {'form': form, 'ciudad': ciudad})


def eliminar_ciudad(request, id_ciudad):
    ciudad = get_object_or_404(ciudad, id=id_ciudad)
    ciudad.delete()
    return redirect('lista_contactos')  # Redirigir a la lista de contactos o donde prefieras


def editar_empresa(request, id_empresa):
    # Obtener la empresa por su NIT
    empresa_obj = get_object_or_404(empresa, nit_empresa=id_empresa)

    if request.method == 'POST':
        # Cargar el formulario con los datos enviados y la instancia de la empresa
        form = EmpresaForm(request.POST, instance=empresa_obj)
        if form.is_valid():
            form.save()  # Guardar los cambios en la base de datos
            return redirect('lista_contactos')  # Redirigir a la lista de contactos o empresas
    else:
        # Cargar el formulario con los datos actuales de la empresa
        form = EmpresaForm(instance=empresa_obj)

    return render(request, 'gestionContactos/formulario_editar_empresa.html', {'form': form, 'empresa': empresa_obj})


def eliminar_empresa(request, id_empresa):
    empresa = get_object_or_404(empresa, nit_empresa=id_empresa)
    empresa.delete()
    return redirect('lista_contactos')  # Redirigir a la lista de contactos o donde prefieras


def lista_empresas(request):
    empresas = empresa.objects.all()  # Obtener todas las empresas de la base de datos
    return render(request, 'gestionContactos/lista_empresas.html', {'empresas': empresas})


def lista_ciudades(request):
    ciudades = ciudad.objects.all()  # Obtener todas las ciudades de la base de datos
    return render(request, 'gestionContactos/lista_ciudades.html', {'ciudades': ciudades})
