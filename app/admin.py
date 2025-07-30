from django.contrib import admin

from app.models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass
