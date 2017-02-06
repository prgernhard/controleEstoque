from django.contrib import admin

# Register your models here.
from app.models import *


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "sku", "criado_em", "editado_em")

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ("nome", "prmedio")

class ItemAdmin(admin.ModelAdmin):
    list_display = ("produto", "quantidade", "criado_em", "editado_em")

class SafraAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nome", "dtinicio", "dtfim")
class ServicosAdmin(admin.ModelAdmin):
    list_display = ("nome", "dtinicio", "dtfim")

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Produtos, ProdutosAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Balcao)
admin.site.register(Safra, SafraAdmin)
admin.site.register(Servicos, ServicosAdmin)
