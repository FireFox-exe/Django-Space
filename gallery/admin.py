from django.contrib import admin
from gallery.models import Fotografia

class ListantadoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_editable = ("publicada",)
    list_per_page = (4)

admin.site.register(Fotografia, ListantadoFotografias)