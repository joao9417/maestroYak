from django.db import models

# Create your models here.

class ciudad(models.Model):
    codigo = models.AutoField(primary_key=True)  # Genera automáticamente un valor único incremental
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return "{0}".format(self.nombre)


class empresa(models.Model):
    nit_empresa = models.CharField(max_length=20, primary_key=True)
    nombre_empresa = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_empresa


class contacto_persona(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    nombre_contacto = models.CharField(max_length=30)
    apellido_contacto = models.CharField(max_length=30)
    ciudad_contacto = models.ForeignKey(ciudad, null=False, blank=False, on_delete=models.CASCADE)
    empresa_contacto = models.ForeignKey(empresa, null=False, blank=False, on_delete=models.CASCADE)
    comentario = models.TextField(blank=True, null=True)  # Nuevo campo para comentarios

    def nombre_completo(self):
        txt = "{0} {1}"
        return txt.format(self.nombre_contacto, self.apellido_contacto)
    
    def __str__(self):
        return self.nombre_completo()
    

class telefono(models.Model):
    persona = models.ForeignKey(contacto_persona, null=False, blank=False, on_delete=models.CASCADE)
    numero_telefono = models.CharField(max_length=15)

    def __str__(self):
        return "{0} ({1})".format(self.numero_telefono, self.persona)


class email(models.Model):
    persona = models.ForeignKey(contacto_persona, null=False, blank=False, on_delete=models.CASCADE)
    email_contacto = models.EmailField(max_length=50)

    def __str__(self):
        return "{0} ({1})".format(self.email_contacto , self.persona)


