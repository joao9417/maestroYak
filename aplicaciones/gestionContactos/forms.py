from django import forms
from .models import contacto_persona, telefono, email, empresa, ciudad

class ContactoPersonaForm(forms.ModelForm):
    class Meta:
        model = contacto_persona
        fields = ['nombre_contacto', 'apellido_contacto', 'ciudad_contacto', 'empresa_contacto', 'comentario']  # Agregar 'comentario'

class TelefonoForm(forms.ModelForm):
    class Meta:
        model = telefono
        fields = ['numero_telefono']

class EmailForm(forms.ModelForm):
    class Meta:
        model = email
        fields = ['email_contacto']

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = empresa
        fields = ['nit_empresa', 'nombre_empresa']  # Asegúrate de incluir los campos correctos

class CiudadForm(forms.ModelForm):
    class Meta:
        model = ciudad
        fields = ['codigo', 'nombre']