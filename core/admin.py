from django.contrib import admin

# Register your models here.

from .models import Grupo,Contato

admin.site.register(Grupo)
admin.site.register(Contato)