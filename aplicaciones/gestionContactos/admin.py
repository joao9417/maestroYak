from django.contrib import admin

# Register your models here.

from .models import ciudad, empresa, contacto_persona, telefono, email

admin.site.register(ciudad)
admin.site.register(empresa)
admin.site.register(contacto_persona)
admin.site.register(telefono)
admin.site.register(email)
