from django.contrib import admin

# Register your models here.
from app.models import *

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ("nome", "prmedio")

class SafraAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nome", "dtinicio", "dtfim")
class ServicosAdmin(admin.ModelAdmin):
    list_display = ("nome", "dtinicio", "dtfim")


admin.site.register(Produtos, ProdutosAdmin)

admin.site.register(Safra, SafraAdmin)
admin.site.register(Servicos, ServicosAdmin)



