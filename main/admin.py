from django.contrib import admin
from .models import Usuario
from django.utils.html import format_html

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'numero_celular', 'ver_foto')

    def ver_foto(self, obj):
        if obj.foto:
            return format_html('<img src="{}" width="50"/>', obj.foto.url)
        return "Sin foto"
    ver_foto.short_description = 'Foto'